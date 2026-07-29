import os
import cv2
import numpy as np
from deepface import DeepFace


def main():
    # Directorio base donde se encuentra el script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    conocidos_dir = os.path.join(base_dir, "conocidos")
    pruebas_dir = os.path.join(base_dir, "pruebas")
    resultados_dir = os.path.join(base_dir, "resultados")

    # Asegurar que la carpeta de resultados exista
    os.makedirs(resultados_dir, exist_ok=True)

    print("=== PROGRAMA DE RECONOCIMIENTO FACIAL ===")
    print("Cargando y codificando personas conocidas...")

    # Pre-calcular embeddings de las personas conocidas
    conocidos_embeddings = {}

    if os.path.exists(conocidos_dir):
        for archivo in os.listdir(conocidos_dir):
            if archivo.lower().endswith(".png"):
                nombre_persona = os.path.splitext(archivo)[0].capitalize()
                path_imagen = os.path.join(conocidos_dir, archivo)
                try:
                    reps = DeepFace.represent(path_imagen, enforce_detection=False)
                    if reps:
                        conocidos_embeddings[nombre_persona] = reps[0]["embedding"]
                        print(f" - Registrada persona conocida: {nombre_persona}")
                except Exception as e:
                    print(f"Error procesando {archivo}: {e}")

    print(f"\nSe cargaron {len(conocidos_embeddings)} personas conocidas.")

    if not os.path.exists(pruebas_dir):
        print(f"Error: La carpeta '{pruebas_dir}' no existe.")
        return

    # Listar imágenes de prueba
    archivos_prueba = [
        f for f in sorted(os.listdir(pruebas_dir))
        if f.lower().endswith((".png", ".jpg", ".jpeg")) and not f.startswith(".")
    ]

    total_fotos = len(archivos_prueba)
    personas_conocidas_encontradas = set()

    print(f"\nAnalizando {total_fotos} fotos en la carpeta 'pruebas'...\n")

    for i, archivo in enumerate(archivos_prueba, 1):
        path_foto = os.path.join(pruebas_dir, archivo)
        imagen = cv2.imread(path_foto)
        if imagen is None:
            print(f"[{i}/{total_fotos}] No se pudo cargar {archivo}")
            continue

        try:
            # Extraer todas las caras y sus embeddings de la foto de prueba
            reps_prueba = DeepFace.represent(path_foto, enforce_detection=False)
        except Exception as e:
            print(f"[{i}/{total_fotos}] Error procesando {archivo}: {e}")
            reps_prueba = []

        print(f"[{i}/{total_fotos}] {archivo}: {len(reps_prueba)} rostro(s) detectado(s).")

        for rep in reps_prueba:
            area = rep["facial_area"]
            x, y, w, h = area["x"], area["y"], area["w"], area["h"]
            emb_prueba = rep["embedding"]

            mejor_coincidencia = None
            menor_distancia = float("inf")

            # Comparar contra cada persona conocida usando distancia coseno
            for nombre_conocido, emb_conocido in conocidos_embeddings.items():
                dot_product = np.dot(emb_prueba, emb_conocido)
                norm_a = np.linalg.norm(emb_prueba)
                norm_b = np.linalg.norm(emb_conocido)
                distancia = 1.0 - (dot_product / (norm_a * norm_b))

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    mejor_coincidencia = nombre_conocido

            # Umbral de verificación VGG-Face (distancia coseno <= 0.40)
            umbral = 0.40
            if menor_distancia <= umbral and mejor_coincidencia is not None:
                etiqueta = mejor_coincidencia
                color = (0, 255, 0)  # Verde en BGR
                personas_conocidas_encontradas.add(mejor_coincidencia)
            else:
                etiqueta = "Desconocido"
                color = (0, 0, 255)  # Rojo en BGR

            # Dibujar rectángulo en la foto
            cv2.rectangle(imagen, (x, y), (x + w, y + h), color, 2)

            # Escribir nombre o etiqueta arriba del rectángulo
            pos_y = max(y - 10, 25)
            cv2.putText(
                imagen,
                etiqueta,
                (x, pos_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2,
                cv2.LINE_AA
            )

        # Guardar la foto procesada y etiquetada en la carpeta 'resultados'
        path_resultado = os.path.join(resultados_dir, archivo)
        cv2.imwrite(path_resultado, imagen)

        # Mostrar foto procesada en la ventana de OpenCV
        nombre_ventana = f"Reconocimiento Facial - {archivo} ({i}/{total_fotos})"
        cv2.imshow(nombre_ventana, imagen)
        print(f" -> Guardada en 'resultados/{archivo}'")
        print(" -> Presione cualquier tecla en la ventana de la imagen para continuar...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Resumen final en la consola
    print("\n" + "=" * 45)
    print("RESUMEN FINAL DE RECONOCIMIENTO")
    print("=" * 45)
    print(f"Fotos analizadas en total: {total_fotos}")
    print(f"Personas conocidas distintas encontradas: {len(personas_conocidas_encontradas)}")
    if personas_conocidas_encontradas:
        print(f"Personas identificadas: {', '.join(sorted(personas_conocidas_encontradas))}")
    print("=" * 45)


if __name__ == "__main__":
    main()

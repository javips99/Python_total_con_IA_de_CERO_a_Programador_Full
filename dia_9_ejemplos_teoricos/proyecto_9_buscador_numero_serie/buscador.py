import os
import re
import datetime
import time
import math

# --- 1. CABECERA Y FECHA ---
fecha_hoy = datetime.datetime.now().strftime("%d/%m/%y")
print("-" * 50)
print(f"Fecha de hoy: {fecha_hoy}")
patron = r"N\w{3}-\d{5}"
print("_" * 50)


# --- 2. CONFIGURACIÓN INICIAL ---
lista_archivos = []
inicio = time.time()


# --- 3. BÚSQUEDA Y EXTRACCIÓN ---
for raiz, carpetas, archivos in os.walk("Mi_Gran_Directorio"):

    for archivo in archivos:

        ruta_completa = os.path.join(raiz, archivo)
        
        # 2. Abrimos el archivo en modo lectura ("r")
        archivo_abierto = open(ruta_completa, "r")
        
        # 3. Guardamos todo el texto del archivo en una variable
        texto = archivo_abierto.read()

        resultado = re.search(patron, texto)

        if resultado:
            numero_encontrado = resultado.group()
            lista_archivos.append((archivo, numero_encontrado))


        archivo_abierto.close()



# --- 4. CÁLCULOS FINALES ---
final = time.time()
duracion = math.ceil(final - inicio)
print(f"Tiempo transcurrido: {duracion} segundos")



# --- 5. PRESENTACIÓN DE LA TABLA ---
print(f"{'ARCHIVO':<30} | {'NRO. SERIE'}")
print("-" * 50)

for archivo, numero in lista_archivos:
    print(f"{archivo:<30} | {numero}")

print("-" * 50)
print(f"Números encontrados: {len(lista_archivos)}")
print(f"Tiempo de búsqueda: {duracion} segundos")
print("-" * 50)
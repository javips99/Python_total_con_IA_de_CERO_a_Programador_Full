from deepface import DeepFace


resultado = DeepFace.represent(img_path="cara1.png")

codificacion = resultado[0]["embedding"]

print(len(codificacion))



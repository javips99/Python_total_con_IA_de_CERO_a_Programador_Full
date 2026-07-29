from deepface import DeepFace


resultado = DeepFace.verify(img1_path="cara2.jpg", img2_path="cara3.jpg")

for c, v in resultado.items():
    print(f"{c}: {v}")



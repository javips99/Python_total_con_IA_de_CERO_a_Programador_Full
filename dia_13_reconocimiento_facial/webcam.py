from deepface import DeepFace
import cv2

camara = cv2.VideoCapture(0)
camara.read()
exito, frame = camara.read()

camara.release()
if exito:
    cv2.imwrite("captura.jpg", frame)
    resultado = DeepFace.verify(img1_path="captura.jpg", img2_path="cara2.jpg", enforce_detection=False)
    
    if resultado['verified']:
        color = (0, 255, 0)
        texto = "La persona es la misma"
    else:
        color = (0, 0, 255)
        texto = "La persona no es la misma"

    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
    cv2.imshow("Verificacion", frame)
    cv2.waitKey(0)


    
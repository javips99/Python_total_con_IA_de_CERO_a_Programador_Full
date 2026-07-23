import os # sirve para obtener la ruta del directorio actual
import shutil # sirve para mover archivos de un directorio a otro
import send2trash # sirve para enviar archivos a la papelera de reciclaje

print("La ruta del directorio actual es:", os.getcwd()) # sirve para obtener la ruta del directorio actual

shutil.move("ruta/archivo a mover", "ruta/destino") # sirve para mover archivos de un directorio a otro

send2trash.send2trash("ruta/archivo a eliminar") # sirve para enviar archivos a la papelera de reciclaje

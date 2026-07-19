
import os

ruta = os.getcwd() # obtener el directorio actual de trabajo
print(ruta)

###

ruta = os.chdir("Ruta a la que queremos acceder") # acceder a otro directorio 
print(ruta)
archivo = open("nombre del archivo del directorio")
print(archivo.read())
archivo.close()

### crear directorios

ruta = os.makedirs("USER/proyectos_vscode/Python_total_con_IA_de_CERO_a_Programador_Full/dia_6_ejemplos_teoricos/otra_carpeta") # crear nueva carperta  
print(ruta)

### obtener solo el nombre del archivo
ruta = "USER/proyectos_vscode/Python_total_con_IA_de_CERO_a_Programador_Full/dia_6_ejemplos_teoricos/prueba.txt"
archivo = os.path.basename(ruta)
print(archivo)

###
### Obtener el nombre del archivo y la ruta
ruta = "USER/proyectos_vscode/Python_total_con_IA_de_CERO_a_Programador_Full/dia_6_ejemplos_teoricos/prueba.txt"
directorio = os.path.dirname(ruta)
print(directorio)

### obtener una tupla con la direccion y el nombre del archivo

ruta = "USER/proyectos_vscode/Python_total_con_IA_de_CERO_a_Programador_Full/dia_6_ejemplos_teoricos/prueba.txt"
mi_ruta = os.path.split(ruta)
print(mi_ruta)

### eliminar carpetas
os.rmdir("ruta de la carpeta a eliminar")
from pathlib import Path

### Algunos metodos
carpeta = Path("ruta del archivo")
print(carpeta.read_text()) # no es necesario pasarle parametros (metodo)
print(carpeta.name) # esto es una propiedad que nos devuelve el nombre del archivo
print(carpeta.suffix) # para mustrar la terminacion del archivo (.txt, .doc etc)
print(carpeta.stem) # es una propiedad que nos devuelve el nombre del archivo sin la extension
print(carpeta.exists()) # obtendremos un booleano con el que podremos sabersi el archvivo existe 

#### Hay muchos metodos mas


base = Path.home()
print(base)
guia = Path("Barcelona", "Sagrada Familia")
print(guia)






# Ejercicios

'''




'''
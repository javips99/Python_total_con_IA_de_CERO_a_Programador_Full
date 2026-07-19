
# Abrimos en modo escritura (w) para crear/modificar
archivo = open("prueba1.txt", "w")
archivo.write("Soy una nueva linea")
archivo.close() # Es obligatorio cerrar para que los cambios se guarden en el disco

# Abrimos de nuevo, pero ahora en modo lectura (r)
archivo = open("prueba1.txt", "r")
print(archivo.read())

archivo.close() # Cerramos siempre al terminar

# modo Añadir "a"
archivo = open("prueba1.txt", "a")

archivo.write("\nSoy otra linea")

archivo = open("prueba1.txt", "r")
print(archivo.read())

archivo.close()


# ejercicios

'''
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

'''
mi_archivo = open("mi_archivo.txt","w")
mi_archivo.write("Nuevo texto")

mi_archivo.close()

mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())

mi_archivo.close()

'''
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

'''
mi_archivo = open("mi_archivo.txt","a")
mi_archivo.write("Nuevo inicio de sesión")

mi_archivo.close()

mi_archivo = open("mi_archivo.txt","r")
print(mi_archivo.read())

'''
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt"
Inserta un tabulador entre cada elemento de la lista para separarlos.
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
Imprime el contenido completo de "registro.txt" al finalizar.
Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. 
También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

'''
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + "\t")

registro.close()

registro = open("registro.txt", "r")
print(registro.read())


from os import system

#limpiar la consola
'''
Para controlar la información mostrada al usuario en consola
podemos limpiarla, eliminando los diferentes mensajes que
han aparecido conforme se va ejecutando el programa.

En Unix/Linux/MacOS:
    system("clear")
En DOS/Windows:
    system("cls")
'''
nombre = input("Dime tu nombre ")
edad = input("Dime tu edad ")
system("cls")
print(f"Tu nombre es {nombre} y tienes {edad} años")

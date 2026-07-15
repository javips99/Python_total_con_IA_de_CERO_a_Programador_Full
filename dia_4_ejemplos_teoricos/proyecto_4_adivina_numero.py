
from random import randint

intentos = 0
numero_usuario = 0
aleatorio = randint(1, 100)

nombre = input("¿Cual es tu nombre? ")
print(f"Hola {nombre} he pensado un número entre 1 y 100 y tienes 8 intentos para adivinarlo")

while intentos < 8:
    numero_usuario = int(input(f"Intento {intentos + 1}"))
    intentos += 1

    if numero_usuario not in range(1, 101):
        print("El número debe estar entre 1 y 100. Inténtalo de nuevo.")
    elif numero_usuario < aleatorio:
        print("El número es mayor. Inténtalo de nuevo.")
    elif numero_usuario > aleatorio:
        print("El número es menor. Inténtalo de nuevo.")
    else:
        print(f"Felicitaciones, {nombre}! Adivinaste el número en {intentos + 1} intentos.")
        break

if numero_usuario != aleatorio:
    print(f"Lo siento, {nombre}. El número secreto era {aleatorio}.")


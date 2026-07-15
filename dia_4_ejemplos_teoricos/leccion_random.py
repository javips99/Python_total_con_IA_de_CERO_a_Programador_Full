
### randint

from random import randint, uniform, random, choice, shuffle  # para importar todo usariamos *

aleatorio = randint(1, 50) # numero aleatorio entre 1 y 50
print(aleatorio)

### uniform
aleatorio = round(uniform(1, 50),2) # numero aleatorio entre 1 y 50 de tipo float para evitar demasiados decimales usamos round
print(aleatorio)

### random
aleatorio = random() # numero aleatorio entre 0 y 1
print(aleatorio)

### choice
colores = ["Azul", "Verde", "Rojo", "Amarillo"]
aleatorio = choice(colores) # escoger un elemento aleatorio de una lista
print(aleatorio)

### shuffle
numeros = list(range(5, 50, 5))
shuffle(numeros) # 
print(numeros)

'''
Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10,
y almacena dicho valor en una variable llamada aleatorio

'''
aleatorio = randint(1, 10)
print(aleatorio)

'''
Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1,
y almacena dicho valor en una variable llamada aleatorio

'''
aleatorio = random() # numero aleatorio entre 0 y 1
print(aleatorio)

'''
Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación,
y almacena el nombre escogido en una variable llamada sorteo

'''
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)
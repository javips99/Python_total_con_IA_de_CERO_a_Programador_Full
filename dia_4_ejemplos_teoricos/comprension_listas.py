
# metodo abreviado para obtener las letras de la palabra " python"

lista = [letra for letra in "python"]
print(lista)

###
lista = [n for n in range(0, 21, 2)] # numeros de 0 al 20
print(lista)

###
lista = [n if n * 2 > 10 else "no" for n in range(0, 21, 2)]
print(lista)

###

pies = [10, 20, 30, 40, 50]
metros = [n /3.281 for n in pies]

print(metros)

'''
Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. 
Si bien en programación el camino correcto es el que devuelve el resultado correcto, 
te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. 
¡Pueden resultarte muy útiles en tu práctica profesional!
Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

'''
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n ** 2 for n in valores]
print(valores_cuadrado)

'''
Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

'''
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)

'''
Para la siguiente lista de temperaturas en grados Fahrenheit, 
expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius.
La conversión entre tipo de unidades es la siguiente:
°C = (°F - 32) * (5/9)
o expresado de otro modo:
(grados_fahrenheit-32)*(5/9)
La lista de temperaturas es la siguiente:
temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius

'''
temperatura_fahrenheit = [32, 212, 275] 
grados_celsius = [(n -32) * (5/9) for n in temperatura_fahrenheit ]
print(grados_celsius)
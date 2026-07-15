
# loop for

nombres = ["Juan", "Ana", "Carlos", "Belen", "Fran"]
for e in nombres:
    print("Hola")

###
mi_lista = ["a", "b", "c", "d"]
for l in mi_lista:
    print("La letra es: " + l)

### para ver el indice
mi_lista = ["a", "b", "c", "d"]
for letra in mi_lista:
    numero_letra = mi_lista.index(letra)
    print(f"La letra es: {letra} tiene el indice {numero_letra}")

###
lista = ["Pablo", "Luis", "Fede", "Laura", "Julia"]

for nombre in lista:
    if nombre.startswith("L"):
        print(nombre)
    else:
        print("Este nombre no comienza con 'L'")

### 
numeros = [1, 2, 3, 4, 5]
valor = 0

for numero in numeros:
    valor = valor + numero
    print(valor)

###
palabra = "python"

for letra in palabra:
    print(letra)

###

for primero, segundo in [[1,2],[3,4],[5,6]]:
    print(primero)
    print(segundo)

###
dic = {"clave1":"A", "clave2":"B","clave3": "C"}

for item in dic.items():
    print(item)

for item in dic.keys():
    print(item)

for item in dic.values():
    print(item)

'''
Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
Por ejemplo: "Hola María"
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

'''
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for a in alumnos_clase:
    print("Hola " + a)

'''
Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
'''
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for suma in lista_numeros:
    suma_numeros = suma_numeros + suma
    print(f"La suma de los numeros es: {suma_numeros}")

'''
Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* 
por separado en las variables suma_pares y suma_impares respectivamente:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par,
y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)

'''
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for elemento in lista_numeros:
    if elemento % 2 == 0:
        suma_pares += elemento
    else:
        suma_impares += elemento

print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")




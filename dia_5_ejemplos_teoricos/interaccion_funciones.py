
from random import shuffle

# lista inicial

palitos = ["-", "--", "---", "----"]

# mezclar palitos

def mezclar (lista):
    shuffle(lista)
    return lista

# comprobamos que funciona la mezcla de elementos

#### palitos_mezclados = mezclar(palitos)
#### print(palitos_mezclados)


# pedir al usuario que ekija 

def probar_suerte():
    intento = " "
    
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un número del 1 al 4: ")
    
    return int(intento)    

# comprobar el intento del usuario

def comprobar_intento (lista, intento):

    seleccion = intento -1
    if lista[seleccion] == "-":
        print("¡A lavar los platos! ")
    else:
        print("Esta vez te salvaste")

    print(f"Te ha tocado {lista[seleccion]}")

palitos_mezclados = mezclar(palitos)
numero_elegido = probar_suerte()
comprobar_intento(palitos_mezclados, numero_elegido)

### Ejercicios

'''
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:
La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).
Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.
Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:
Si la suma es menor o igual a 6:
"La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
"La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar

'''

from random import randint

def lanzar_dados ():
    dado1 = 0
    dado2 = 0
    dado1 = randint(1, 6)
    dado2 = randint(1,6)
    return (dado1,dado2)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

d1 = 0
d2 = 0

d1, d2 = lanzar_dados()
resultado = evaluar_jugada(d1,d2)
print(resultado)

'''
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), 
y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) 
y eliminando el valor más alto. El orden de los elementos puede modificarse.
Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

'''

lista_numeros = [8, 32, 25, 25, 45, 8, 25, 47, 95, 8]

def reducir_lista(lista_numeros):
    lista_unica = []
    for numero in lista_numeros:
        if numero not in lista_unica:
            lista_unica.append(numero)
    
    lista_unica.remove(max(lista_unica))
    return lista_unica

def promedio(lista_unica):
    return sum(lista_unica) / len(lista_unica)

lista_limpia = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_limpia)

print(f"La lista reducida es: {lista_limpia}")
print(f"El promedio de la lista es: {resultado_promedio}")

'''
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). 
Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
Crea una segunda función (llamada probar_suerte), que tome dos argumentos: 
    -El primero, debe ser el resultado del lanzamiento de la moneda. 
    -El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", 
y eliminarla (devolverla como lista vacía []).
Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.
Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

'''
from random import choice

lista_numeros = [ 5, 27, 6, 78, 95, 2]

def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    return moneda


def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
    
resultado_lanzamiento = lanzar_moneda()
lista_final = probar_suerte(resultado_lanzamiento, lista_numeros)
print(lista_final)


### Esta funcion, comprueba si un número tiene exactamente tres cifras (el primer print sera True y el segundo False)
def comprobar_3_cifras(numero):
    
    return numero in range(100, 1000)

resultado = comprobar_3_cifras(685)
print (resultado)

resultado = comprobar_3_cifras(23)
print (resultado)

### comprueba si dentro de la lista existe al menos un número de tres cifras

mi_lista = [55, 99, 6000]
def comprobar_3_cifras(lista):
    for l in lista:
        if l in range(100, 1000):
            return True
    
    return False   
        
resultado = comprobar_3_cifras(mi_lista)
print (resultado)

### muestra los numeros de 3 cifras que hay en la lista

mi_lista = [555, 99, 800]

def comprobar_3_cifras(lista):
    lista_3_cifras = []

    for l in lista:
        if l in range(100, 1000):
            lista_3_cifras.append(l)
    
    return lista_3_cifras 
        
resultado = comprobar_3_cifras(mi_lista)
print (resultado)

### Ejercicios
'''
Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.
No invoques la función, solo es necesario definirla.

'''
lista_numeros = [8, -5, 64, -58, 45]

def todos_positivos(lista_numeros):
    for l in lista_numeros:
        if l < 0:
            return False
        
    return True
resultado = todos_positivos(lista_numeros)
print (resultado)

'''
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.

'''
lista_numeros = [1, 4, 3, 2]

def suma_menores(lista_numeros):
    suma = 0
    for elemento in lista_numeros:
        if elemento > 0 and elemento < 1000:
            suma += elemento

    return suma

resultado = suma_menores(lista_numeros)
print (resultado)

'''
Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), 
y devuelva el resultado de dicha cuenta.

'''

lista_numeros = [12, 21 ,14, 3, 5, 9, 8]

def cantidad_pares(lista_numeros):
    suma_pares = 0      # aqui se iran añadiendo la cantidad de numeros pares que hay en la lista
    for elemento in lista_numeros:
        if elemento % 2 == 0:
            suma_pares +=1
    
    return suma_pares

resultado = cantidad_pares(lista_numeros)
print(resultado)

# Ejercicio 1

'''
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio
'''
def devolver_distintos(num1, num2, num3):
           
    total_suma = sum([num1,num2,num3])

    if total_suma > 15:
        return max([num1,num2,num3])  
                                      
    elif total_suma < 10:
        return min([num1, num2, num3])
    else:
        return sorted([num1,num2,num3])[1]

print(devolver_distintos(2,4,5))

# Ejercicio 2

'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d,'e','i','n','o','r','t']

'''
palabra = "alfabetico"

def letras_unicas(palabra):
    return sorted(set(palabra))

print (letras_unicas(palabra))

# Ejercicio 3

'''
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False

'''
def cantidad_indefinida(*args):
    
    for indice in range(len(args)-1):
        if args [indice] == 0 and args[indice + 1] == 0 : 
            return True
    
    return False
print(cantidad_indefinida(25, 78, 35, 0,0, 57, 23, 68))

# Ejercicio 4

'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.

'''

def contar_primos(numero):
    primos = []
    for elemento in range(2,numero +1):
        for divisor in range(2, elemento):
            if elemento % divisor == 0:
                break
        else:
            primos.append(elemento)
    print(primos)
    return len(primos)

contar_primos(50)
            


# Ejemplo
def suma (*args):
    return sum(args)
   

print(suma(4, 5, 6, 28, 32, 45, 125))

### ejercicios

'''
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, 
y que retorne la suma de sus valores al cuadrado.
Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

'''

def suma_cuadrados(*args):
    resultado = 0
    for elemento in args:
        resultado += elemento ** 2
    return resultado        

print(suma_cuadrados(1, 2, 3, 4))

'''
Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, 
y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, 
los considere a todos -negativos y positivos- como positivos)

'''
def suma_absolutos(*args):
    resultado = 0
    for elemento in args:
        resultado += abs(elemento)
    return resultado        

print(suma_absolutos(1, 2, -3, -4, 10))

'''
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, 
y a continuación, una cantidad indefinida de números.
La función debe devolver el siguiente mensaje:
"{nombre}, la suma de tus números es {suma_numeros}"

'''
def numeros_persona(nombre,*args):
    
    suma_numeros = sum(args)
    return (f"{nombre}, la suma de tus números es {suma_numeros}")

print(numeros_persona("Fco. javier", 75, 20, 65))

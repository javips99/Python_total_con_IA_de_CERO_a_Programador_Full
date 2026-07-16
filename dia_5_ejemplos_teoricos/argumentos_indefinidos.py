
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
import math
# Este módulo proporciona acceso a las funciones matemáticas. Algunos metodos útiles son:

resultado = math.floor(89.4)
print(resultado)  # Salida: 89

resultado = math.ceil(89.4)
print(resultado)  # Salida: 90

resultado = math.trunc(89.4)
print(resultado)  # Muestra la parte entera de un número

resultado = math.pi
print(resultado)  # Salida: 3.141592653589793 (numero pi)

### Ejercicios

'''
Obtén el logaritmo base 10 del número 25, y almacena el resultado en la variable resultado.
Puedes utilizar el método math.log10()
Puedes consultar el enlace anterior si quieres conocer más acerca del logaritmo decimal.

'''
resultado = math.log10(25)
print("El logaritmo base 10 de 25 es:", resultado)

'''
Obten la raíz cuadrada de pi con la constante math.pi y el método math.sqrt(). 
Almacena el resultado obtenido en la variable resultado

'''
resultado = math.sqrt(math.pi)
print("La raíz cuadrada de pi es:", resultado)

'''
Encuentra el factorial de 7 y almacena el resultado en la variable resultado.
El método a utilizar es factorial()

'''
resultado = math.factorial(7)
print("El factorial de 7 es:", resultado)

# operadores de comparacion

# < menor que  <= menor o igual que
# > msyor que  >= mayor o igual que
# == igual a   != diferente de

mi_variable = "hola mundo"

mi_bool = mi_variable == "hola mundo"

print(mi_variable)
print(mi_bool)
print(type(mi_bool))

mi_bool = 10 == 10
print(mi_bool)
mi_bool = 10 == 4 + 6
print(mi_bool)
mi_bool = 10 == 5
print(mi_bool)

print("\n")
mi_bool = "blanco" == "Blanco".lower()
print(mi_bool)

'''
Práctica Operadores de Comparación
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente.
Verifica si num1 es mayor o igual que num2 y almacena el resultado 
de dicha comparación en una variable llamada mi_bool

'''
num1 = 36
num2 = 17

mi_bool = num1 >= num2
print(mi_bool)

'''
Práctica Operadores de Comparación
Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25
Dentro de num2, almacena el número 5.
Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

'''
num1 = 25 ** 0.5
num2 = 5
mi_bool = num1 == num2 
print(mi_bool)

'''
Práctica Operadores de Comparación 3
Crea dos variables (num1 y  num2):
Dentro de num1, almacena el resultado de la operación 64 x 3
Dentro de num2, almacena el resultado de la operación 24 x 8
Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.

'''
num1 = 64 * 3
num2 = 24 * 8
mi_bool = num1 != num2
print(mi_bool)
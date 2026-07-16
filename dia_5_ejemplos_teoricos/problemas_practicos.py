
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
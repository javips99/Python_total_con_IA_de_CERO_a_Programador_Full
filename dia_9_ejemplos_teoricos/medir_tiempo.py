import time,timeit

# time se utiliza para medir el tiempo de ejecución de un bloque de código (como un cronometro, inicio y final).
# timeit se utiliza para medir ejecuciones muy breves repitiendolas muchas veces


def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
            lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
# Código a medir
prueba_for(1000000)
final = time.time()
print("Tiempo transcurrido:", final - inicio, "segundos")

inicio = time.time()
# Código a medir
prueba_while(1000000)
final = time.time()
print("Tiempo transcurrido:", final - inicio, "segundos")


### timeit
# timeit.timeit() ejecuta el código muchas veces y devuelve el tiempo total de ejecución

declaracion_for = "prueba_for(1000000)"
mi_setup_for = """
def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista
""" 

duracion_for = timeit.timeit(declaracion_for, setup=mi_setup_for, number=100)
print("Tiempo transcurrido con timeit para for:", duracion_for, "segundos")

declaracion_while = "prueba_while(1000000)"
mi_setup_while = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""
duracion_while = timeit.timeit(declaracion_while, setup=mi_setup_while, number=100)
print("Tiempo transcurrido con timeit para while:", duracion_while, "segundos")
# Forma que hemos usado anteriosmente para crear una lista

def mi_funcion():
    lista = []
    for i in range(1, 5):
        lista.append(i * 10)
    return lista

# Forma de crear un generador
def mi_generador():

    for i in range(1, 5):
        yield i * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))

print("Esta linea no hace nada")

print(next(g))


### Otro ejemplo de generador

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()
print(next(g))
print(next(g))


### Ejercicios

'''
Crea un generador (almacenado en la variable generador) 
que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, 
y entregando un número consecutivo superior cada vez que sea llamada mediante next.
Pista: Utiliza un loop while para realizar este ejercicio.

'''
def mi_generador():
    x = 1
    while True:
        yield x
        x += 1

generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))

'''
Crea un generador (almacenado en la variable generador) que sea capaz de devolver 
de manera indefinida múltiplos de 7, iniciando desde el mismo 7, 
y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...)

'''
def mi_generador():
    x = 7
    while True:
        yield x
        x += 7

generador = mi_generador()
print(next(generador))
print(next(generador))
print(next(generador))

'''
Crea un generador que reste una a una las vidas de un personaje de videojuego, 
y devuelva un mensaje cada vez que sea llamado:
"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
Almacena el generador en la variable perder_vida

'''
def vida_personaje():
    vidas = "Te quedan 3 vidas"
    yield vidas

    vidas = "Te quedan 2 vidas"
    yield vidas

    vidas = "Te queda 1 vida"
    yield vidas
    
    vidas = "Game Over"
    yield vidas

perder_vida = vida_personaje()

def generador_perfumeria():
    x = 1
    while True:
        yield f"P-{x}"
        x += 1

perfumeria = generador_perfumeria()
print(next(perfumeria))
print(next(perfumeria))
print(next(perfumeria))

def generador_farmacia():
    x = 1
    while True:
        yield f"F-{x}"
        x += 1

farmacia = generador_farmacia()
print(next(farmacia))
print(next(farmacia))
print(next(farmacia))

def generador_cosmeticos():
    x = 1
    while True:
        yield f"C-{x}"
        x += 1

cosmeticos = generador_cosmeticos()
print(next(cosmeticos))
print(next(cosmeticos))
print(next(cosmeticos))

def decorador_turnos(funcion_original):
    def funcion(generador):
        print("Su turno es: ")
        funcion_original(generador)
        print("Aguarde y será atendido")

    return funcion

@decorador_turnos
def mostrar_turno(generador):
    print(next(generador))



def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

def una_funcion(funcion):
    return funcion

mi_funcion = mayuscula

mi_funcion("Hola Mundo")  # Esto imprimirá "HOLA MUNDO"


def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "mayuscula":
        return mayuscula
    elif tipo == "minuscula":
        return minuscula


opcion = cambiar_letras("mayuscula")
opcion("que tal estás")  # Esto imprimirá "HOLA MUNDO"

opcion = cambiar_letras("minuscula")
opcion("Hola Mundo")  # Esto imprimirá "hola mundo"


#### Decoradores

def decorador(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")

    return otra_funcion
def mayuscula(texto):
        print(texto.upper())

def minuscula(texto):
        print(texto.lower())


@decorador
def mayuscula(texto):
    print(texto.upper())


@decorador
def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorador(mayuscula)
minuscula_decorada = decorador(minuscula)

mayuscula("aprender a programar")  # Esto imprimirá "HOLA" y "ADIOS" alrededor del texto en mayúsculas
minuscula("APRENDER A PROGRAMAR")  # Esto imprimirá "HOLA"
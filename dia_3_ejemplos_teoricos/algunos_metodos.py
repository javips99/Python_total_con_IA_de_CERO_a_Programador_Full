# mas metodos python
# upper
texto = "Este es el texto de Javier"
resultado = texto.upper()
print(resultado)

# lower
texto = "ESTE ES EL TEXTO DE JAVIER"
resultado = texto.lower()
print(resultado)

# split (separar cada palabra)
texto = "Este es el texto de Javier"
resultado = texto.split()
print(resultado)

# join (para unir)
a = "Aprender"
b = "Python"
c = "es"
d = "genial"

e = " ".join([a,b,c,d])
print(e)


# find (encontrar)
texto = "Este es el texto de Javier"
resultado = texto.find("g") # si no lo encuentra devuelbe -1
print(resultado)

# replace
texto = "Este es el texto de Javier"
resultado = texto.replace("Javier", "Francisco Javier")
print(resultado)


lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(["La","legibilidad","cuenta."]))
# ejercicio:
# Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

"""los siguientes pares de palabras:

"difícil" a "fácil"

"mala" a "buena"
"""

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil", "fácil").replace("mala", "buena"))

# Propiedades de String

poema = "Mil pequeños peces blancos\n como si hirviera\n el color del agua"
print(poema)

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

print("agua" in poema) # comprobar si la palabra agua esta en el poema

print(len(poema))

# ejercicio Verifica si la palabra "agua" 
# no se encuentra en el siguiente haiku. Debes imprimir el booleano.
haiku = """
Tierra mojada,

mis recuerdos de viaje

entre las lluvias"""

print("agua" is not haiku)

# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

print(len("electroencefalografista"))
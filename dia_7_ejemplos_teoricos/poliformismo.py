
class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Muu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        for i in range(0, 3):
            print(f"Bee{i + 1}")

vaca1 = Vaca("Lola")
oveja1 = Oveja("Dolly")

vaca1.hablar()
oveja1.hablar()

# Otra forma de hacerlo y obtener el mismo resultado es:

animales_granja = [vaca1, oveja1]
for animal in animales_granja:
    animal.hablar()

# otra forma de hacerlo es:

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)

### Ejercicios

'''
La función incorporada en Python len() tiene un comportamiento polimórfico, 
ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), 
devolviendo la cantidad de items o caracteres que lo componen.
Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) 
para cada uno de ellos su longitud con la función len().
Puedes recordar cómo implementar la función len() siguiente enlace: 
https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html

'''
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for i in [palabra, lista, tupla]:
    print(len(i))

    
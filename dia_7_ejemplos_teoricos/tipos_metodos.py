
# Metodos de instancia

class Persona: 
    def mi_nombre(self):
        print("Mi nombre es Juan")
    
persona_uno = Persona()
persona_uno.mi_nombre()

    # acceden y modifican los atributos del objeto
    # aceden a otros metodos
    # modifican el estado del objeto


# Metodos de clase

class Triangulo:
    
    @classmethod
    def area(cls, base, altura):
        print((base * altura) / 2) 
    
    # pueden ser llamaados desde la clase o desde el objeto
    # no pueden acceder a los atributos del objeto

# Metodos estaticos

class Circulo:
    
    @staticmethod
    def area(radio):
        print(3.14 * radio ** 2)
    
    # no aceptan ni self ni cls como primer argumento
    # no pueden modificar el estado del objeto

#### ejemplo

class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print("Pío, pío")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

    def pintar_negro(self):
        self.color = "negro"
        print(f"El pájaro ahora es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pajaro pone {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(4) # Metodo de clase
Pajaro.mirar() # Metodo estatico (sirve para evitar que se modifiquen los atributos del objeto)

mi_pajaro = Pajaro("amarillo", "canario")
print(mi_pajaro.color)

mi_pajaro.pintar_negro() # Metodo de instancia
print(mi_pajaro.color)

mi_pajaro.alas = False
print(mi_pajaro.alas)

### Ejercicios

'''
Crea un método estático respirar() para la clase Mascota. 
Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

'''
class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

'''
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, 
estableciéndolo en True cada vez que es invocado. 
El valor predeterminado del atributo vivo, debe ser False.

'''
class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


'''
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas 
que tiene una instancia de Personaje, 
que cuenta con un atributo de instancia de tipo número, 
llamado cantidad_flechas.

'''
class Personaje:

    @classmethod
    def lanzar_flecha(cls, cantidad_flechas):
        return cantidad_flechas - 1
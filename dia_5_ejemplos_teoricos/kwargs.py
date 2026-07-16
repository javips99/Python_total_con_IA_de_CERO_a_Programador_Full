
### ejemplos

def suma(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        total += valor
    return total

print(suma(x=3, y=4, z=5))

###

def prueba(num1, num2, *args, **kwargs):
    
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    
    for arg in args:
        print(f"arg es igual a {arg}")
        
    for clave, valor in kwargs.items():
        print(f"La clave {clave} es igual a {valor}")


prueba(5, 11, 4, 35, 123, 55, 2654, x=3, y=4, z=5)

### ejercicios
'''
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, 
y devuelva esa cantidad como resultado.

'''
def cantidad_atributos(**kwargs):
    total = 0

    for elemento in kwargs:
        total += 1
    return total

cantidad_atributos(a ="Hola", b = 34, c = 25.33, d = True)

'''
Crea una función llamada lista_atributos que devuelva en forma de lista 
los valores de los atributos entregados en forma de palabras clave (keywords). 
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

'''

def lista_atributos(**kwargs):
    lista_valores = []

    for elemento in kwargs.values():
        lista_valores.append(elemento)
    
    return lista_valores

print(lista_atributos(a ="Hola", b = 34, c = 25.33, d = True))

'''
Crea una función llamada describir_persona, que tome como parámetros su nombre 
y luego una cantidad indetermida de argumentos. 
Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:
Características de María:
color_ojos: azules
color_pelo: rubio
No llames a la función, solamente definela sin llamarla.

'''
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")
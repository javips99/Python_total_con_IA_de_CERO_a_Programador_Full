
from collections import Counter, defaultdict, namedtuple, deque



# Ejemplo de uso de Counter para contar elementos que se repiten en una lista
numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(Counter(numeros))

frase = "Al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1, 1, 1, 1, 2, 2, 3, 3, 3, 4])
print(serie.most_common(2))  # Devuelve los dos elementos más comunes y sus conteos


### Ejemplo de uso de defaultdict
mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}
mi_dc = defaultdict(lambda: "No encontrado", mi_dic)

print(mi_dic["uno"])  # Devuelve "verde"
print(mi_dc["cuatro"])  # Devuelve "No encontrado"


### Ejemplo de uso de namedtuple
persona = namedtuple("Persona", ["nombre", "edad", "ciudad"]) # tupla con nombre y campos
juan = persona("Juan", 30, "Madrid")

print(juan.nombre)  # Devuelve "Juan"
print(juan.edad)    # Devuelve 30
print(juan.ciudad)  # Devuelve "Madrid"

print(juan [1])  # Devuelve el valor del campo edad, que es 30


### Ejercicios

'''
Aplica un Counter (contador) sobre la lista de números entregada a continuación, 
y almacénalo en una variable llamada contador

'''
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)


'''
Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, 
se cargue con el string "Valor no hallado".
Carga el diccionario, al menos, con el siguiente par de datos:
palabra clave = edad
valor = 44
Utiliza el método defaultdict del módulo Collections.

'''
mi_diccionario = {"edad": 44, "nombre": "Alberto"}
mi_diccionario = defaultdict(lambda: "Valor no hallado", mi_diccionario)
print(mi_diccionario["Ciudad"])  # Devuelve "Valor no hallado"

'''
Una cola doblemente terminada o deque (del inglés double ended queue) 
es una estructura de datos lineal que permite insertar y eliminar elementos por ambos extremos.
Investiga más al respecto en cualquier sitio de documentación, 
y a continuación implementa una deque a partir del módulo collections. 
Los elementos iniciales de la lista se brindan a continuación.
["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el nombre lista_ciudades.

'''
lista_ciudades =(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft("Lisboa")  # Agrega "Lisboa" al inicio de la deque
print(lista_ciudades)  # Devuelve deque(['Lisboa', 'Londres',

lista_ciudades.append("Tokio")  # Agrega "Tokio" al final de la deque
print(lista_ciudades)  # Devuelve deque(['Lisboa', 'Londres',
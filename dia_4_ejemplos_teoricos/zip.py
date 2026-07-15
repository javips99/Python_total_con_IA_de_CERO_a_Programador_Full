
nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42, 55, 21]
ciudades = ["Lima", "Madrid", "Mexico", "Lisboa"]

combinados = list(zip(nombres,edades, ciudades)) # solo se imprimen las parejas de elementos
print(combinados)

for nombre, edades, ciudades in combinados:
    print(f"{nombre} tiene {edades} años y vive en {ciudades}")

###
'''
Muestra en pantalla frases como la del siguiente ejemplo:
La capital de Alemania es Berlín
Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

'''

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista_combinada = list(zip(capitales,paises))
for capitales, paises in lista_combinada:
    print(f"La capital de {paises} es {capitales}")

'''
Crea un objeto zip formado a partir de listas, 
de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip

'''
marcas = ["Seat", "Toyota", "Opel", "Ford"]
productos = ["Leon","Corolla", "Astra", "Mondeo"]
mi_zip = zip(marcas,productos)
print(mi_zip)

'''
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), 
y convierte el objeto generado en una lista almacenada en la variable numeros:
uno / um / one
dos / dois / two
tres / três / three
cuatro / quatro / four
cinco / cinco / five
El resultado deberá seguir la estructura:
[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]

'''
español = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
 
numeros = list(zip(español, portugues, ingles))
print(f"Los numeros en Español del 1 al 5 son: {español}\nLos numeros en Portugues del 1 al 5 son: {portugues}\nLos numeros en Inglés del 1 al 5 son: {ingles} \n")

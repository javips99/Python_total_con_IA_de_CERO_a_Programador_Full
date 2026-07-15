
###
menor = min(58, 96, 72, 64, 35)
print(menor)

###
mayor = max(58, 96, 72, 64, 35)
print(mayor)

###
lista = [58, 96, 72, 64, 35]
print(min(lista))

###
lista = [58, 96, 72, 64, 35]
print(f"El menor de la lista es {min(lista)} y el mayor de la lista es {max(lista)}")

###
nombres = "Carlos"
print(min(nombres)) #primero busca las mayusculas por eso aparece en consola "C"

###
nombres = ["Juan", "Pablo", "Alicia", "Carlos"]
print(min(nombres))

###

dic = {"c1":45, "c2": 11}

print(min(dic.values())) #el valor minimo es 11

'''
Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:

'''
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 
valor_maximo = max(lista_numeros)
print(valor_maximo)

'''
Calcula la diferencia entre el valor máximo 
y el mínimo en la siguiente lista de números, 
y almacénalo en una variable llamada rango

'''
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = (max(lista_numeros) - min(lista_numeros))
print(rango)

'''
Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:
Almacena dicho valor en una variable llamada edad_minima.
También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre.
'''
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)
print(ultimo_nombre)
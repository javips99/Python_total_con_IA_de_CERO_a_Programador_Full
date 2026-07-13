# Listas

mi_lista = [1, 2, 3]
mi_otra_lista = [4, 5, 6]
mi_gran_lista = mi_lista + mi_otra_lista

mi_gran_lista[0] = "Uno" # camabiar un elemento de la lista
mi_gran_lista.append(7) # agregar a la lista
mi_gran_lista.pop(2) # eliminar un elemento
elemento_eliminido = mi_gran_lista.pop(2)
print(mi_gran_lista)
print(elemento_eliminido)

mi_lista = [65, 2, 45, 28, 9, 95, 1]
mi_lista.sort() # ordenar lista
print(mi_lista)

mi_lista = [65, 2, 45, 28, 9, 95, 1]
mi_lista.reverse() # ordenar lista al reves
print(mi_lista)


medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)
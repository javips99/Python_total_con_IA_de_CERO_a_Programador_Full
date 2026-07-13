
# dos formas de crearlos

mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set))
print(mi_set)


otro_set = {1, 2, 3,}
print(type(otro_set))
print(otro_set)

s = set([1, 2, 3, 4, 5])
print(len(s))

print(2 in s) #buscar elementos

set1 = {1, 2, 3,}
set2 = {3, 4, 5}
set3 = set1.union(set2)

print(set3)

# agregar elementos

set1.add(6)
print(set1)

# eliminar elementos
set1.remove(6)
print(set1)

sorteo = set1.pop()
print(sorteo)

set1.clear()
print(set1)
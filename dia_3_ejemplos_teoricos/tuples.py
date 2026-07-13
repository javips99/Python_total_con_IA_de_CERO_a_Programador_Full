
# No se puede modificar el contenido

mi_tuple = (1, 2, (3, 4))
otra_tuple = ("javier", 25, "cuellar")

# accedere a un valor de una tuple dentro de otra
print(mi_tuple[2][0])

# si se puede transformar

print(type(mi_tuple))
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

# asignar valores de una tuple a variables

t = (1, 2, 3)
x, y, z = t
print(x, y, z)

# contar elementos
t = (1, 2, 2, 3, 2, 2)
print(t.count(2))

# conocer el indice

t = (1, 2, 2, 3, 2, 2, 4)
print(t.index(4))
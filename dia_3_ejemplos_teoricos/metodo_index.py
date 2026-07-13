# Metodo index y rindex

string = "Hola Mundo"
resultado = string[5]
print(resultado)

string = "Hola Muundo"
resultado = string.index("u") # solo devuelve el indice de la primera ocurrencia que estamos buscando
print(resultado)

string = "Hola Muundo"
resultado = string.rindex("u") # Para buscar desde el final y devolver la primera ocurrencia
print(resultado)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))
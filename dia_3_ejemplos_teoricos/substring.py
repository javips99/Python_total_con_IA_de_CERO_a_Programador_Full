# Substring

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5] # Muestra los valores entre la posicion 2 y 5 sin incluir el caracter 5
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:] # Muestra los valores entre la posicion 2 hasta el final
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[:5] # Muestra los valores entre la posicion 5 (sin incluirlo) hasta el principio
print(fragmento)

texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1] # Muestra los valores desde el final al principio de la cadena
print(fragmento)



frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[9::3])
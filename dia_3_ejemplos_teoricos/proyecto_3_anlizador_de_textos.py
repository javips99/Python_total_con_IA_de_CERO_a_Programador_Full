
texto = input(" Ingrese un texto ")
letras = []
texto = texto.lower()

letras.append(input(" Introduce la primera letra ").lower())
letras.append(input(" Introduce la segunda letra ").lower())
letras.append(input(" Introduce la tercera letra ").lower())

print("\n")
print("Cantidad de palabras")
cantidad_letras1 = texto.count (letras[0])
cantidad_letras2 = texto.count (letras[1])
cantidad_letras3 = texto.count (letras[2])

print(f"Hemos encontrado {cantidad_letras1} veces la letra {letras[0]}")
print(f"Hemos encontrado {cantidad_letras2} veces la letra {letras[1]}")
print(f"Hemos encontrado {cantidad_letras3} veces la letra {letras[2]}")

print("\n")
print("Cantidad de palabras")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

print("\n")
print("Letra inicial y letra final")

letra_inicio = texto[1]
letra_final = texto [-1]

print(f"La letra inicial del texto es '{letra_inicio}")
print(f"La letra final del texto es '{letra_final}")

print("\n")
print("Texto invertido")

palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto invertido es: {texto_invertido}")

print("\n")
print("Buscar la palabra Python")

buscar_python = "python" in texto
dic = {True: "si", False:"no"}
print(f"La palabra Python {dic[buscar_python]} se encuentra en el texto")

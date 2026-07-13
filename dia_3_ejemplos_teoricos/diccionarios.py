
# Diccionarios

mi_diccionario = {"Apellido": "Cuellar", "Nombre": "Francisco Javier", "Edad": "39"}
resultado = mi_diccionario["Nombre"] # para extraer un valor del diccionario
print(resultado)

# imprimir la letra e en mayuscula
dic = {"clave1": ["a","b","c"],
       "clave2": ["d","e","f"]}
print(dic["clave2"][1].upper())

# para ver solo los valores
print(dic.values())

# Formas de iterar
for clave, valor in dic.items():
    print(f"{clave}: {valor}")

# Contar frecuencias
ventas = ["laptop", "mouse", "laptop", "teclado", "laptop", "mouse"]

contador = {}
for producto in ventas:
    contador[producto] = contador.get(producto, 0) + 1

print(contador)


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
 
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

mi_dic = {"nombre": "Karen", "apellido":"Jurgens", "edad": 36, "ocupacion": "Editora", "pais": "Colombia"}

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic ["edad"] = 36
mi_dic ["ocupacion"] = "Editora"
mi_dic ["pais"] = "Colombia"

print(mi_dic)



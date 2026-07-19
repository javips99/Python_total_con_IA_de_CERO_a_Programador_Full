
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"]

registro = open("registro.txt", "a")
for item in registro_ultima_sesion:
    registro.writelines(item + "\t")

registro.close()

registro = open("registro.txt", "r")
print(registro.read())
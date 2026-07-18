
mi_archivo = open("prueba.txt")
'''
print(mi_archivo.read())

primera_linea = mi_archivo.readline()
print(primera_linea)

'''
todas_lineas = mi_archivo.readlines()
print(todas_lineas) # Se covierte en una lista
todas_lineas.pop()
print(todas_lineas)


mi_archivo.close() # Es bueno usarlo siempre para no consumir recursos
# loop while

monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas -1 # normalmente se pone monedas -= 1
else:
    print("Te quedan 0 monedas, se te acabaron las monedas")

###
respuesta = "s"

while respuesta == "s":
    respuesta = input("¿Quieres seguir? (s/n) ")
else:
    print("adios")

###

nombre = input("Cual es tu nombre?")

for letra in nombre:
    if letra == "v":
        break # salir del bucle
    print(letra)

print("\n")

for letra in nombre:
    if letra == "v":
        continue # al llegar a la v la salta y continua
    print(letra)

'''
Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

'''
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

'''
Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos)
con las siguientes condiciones adicionales:
- Si el número es divisible por 5, mostrar dicho número en pantalla 
(¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)

- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla 
(no te olvides de seguir restando para que el programa no corra infinitamente).
'''
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
    continue
'''
Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, 
e interrumpe el flujo en el momento que encuentres un valor negativo:
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
No debes cambiar el orden de la lista.

'''
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for elemento in lista_numeros:
    if elemento >= 0:
        print(elemento)
    elif elemento < 0:
        break


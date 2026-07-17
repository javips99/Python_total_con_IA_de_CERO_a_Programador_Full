
from random import choice

palabras_secretas = ["Coche", "Baúl", "Bicicleta", "Caja", "Ordenador", "Ventilador", "Avión", "Regadera"]

def elegir_palabra(palabras):
    sorteo = choice(palabras)
    return sorteo.lower()
    
def mostrar_guiones(sorteo):
    
    numero_guiones = ["_"] * (len(sorteo))
    return numero_guiones

def pedir_letra():
    letra = ""
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    while  letra not in abecedario or len(letra) != 1: 
        letra = input("Elige una letra: ")
    return letra

def comprobar_letra(letra_usuario, palabra_secreta, numero_guiones, vidas_restantes):
   if letra_usuario in palabra_secreta:
        
        for indice, letra_actual in enumerate(palabra_secreta):
            if letra_actual == letra_usuario:
                numero_guiones[indice] = letra_usuario
   else:
        vidas_restantes -= 1
   return vidas_restantes, numero_guiones

def comprobar_resultado(numero_guiones, vidas_restantes):
    
    if vidas_restantes == 0:
        return "Te quedastes sin vidas, has perdido"
    else:
        if "_" not in numero_guiones:
            return "¡¡¡¡¡Has ganado!!!!!"

palabra_secreta = elegir_palabra(palabras_secretas) 
sorteo = mostrar_guiones(palabra_secreta)   
vidas = 6        

while vidas > 0:
    print(f"Te quedan {vidas} vidas, {sorteo}")
    letra_usuario = pedir_letra()
    vidas, sorteo = comprobar_letra(letra_usuario, palabra_secreta, sorteo, vidas)
    mensaje = comprobar_resultado(sorteo, vidas)
    
    if mensaje != None:
        print(mensaje)
        break
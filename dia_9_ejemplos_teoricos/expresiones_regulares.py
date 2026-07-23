
import re

# Expresiones regulares
# Las expresiones regulares son una herramienta poderosa para buscar y manipular texto. Permiten definir patrones de búsqueda que pueden coincidir con cadenas de texto específicas.

texto = "Si necesitas ayuda llama al (658),- 598- 9977 las 24 horas al servicio de ayuda online"

patron = "ayuda"
busqueda = re.search(patron, texto)

print(busqueda) # Imprime el objeto Match si se encuentra la palabra "ayuda" en el texto, de lo contrario imprime None
print(busqueda.start()) # Imprime la posición inicial de la palabra "ayuda" en el texto
print(busqueda.end()) # Imprime la posición final de la palabra "ayuda" en el texto
print(busqueda.span()) # Imprime una tupla con la posición inicial y final de la palabra "ayuda" en el texto

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span()) # Imprime la posición inicial y final de cada ocurrencia de la palabra "ayuda" en el texto

print(re.findall(patron, texto)) # Imprime una lista con todas las ocurrencias de la palabra "ayuda" en el texto


### otro ejemplo

texto = "llama al 555-123-4567 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d" # Patrón para buscar un número de teléfono en formato xxx-xxx-xxxx
resultado =re.search(patron, texto) # Imprime el objeto Match si se encuentra un número de teléfono en el texto, de lo contrario imprime None
print(resultado)
print(resultado.group()) # Imprime el número de teléfono encontrado en el texto

patron = r"(\d{3})-(\d{3})-(\d{4})" # {} con los corchetres indica la cantidad de dígitos que se esperan en cada grupo del patrón
resultado = re.search(patron, texto)
print(resultado.group(2))

#### otro ejemplo
clave = input("Ingrese su clave: ")
patron = r"\D{1}\w{7}" # Patrón para buscar una clave que comience con una letra y tenga 7 caracteres alfanuméricos
resultado = re.search(patron, clave)
print(resultado) # Imprime el objeto Match si se encuentra una clave que cumpla con el patrón, de lo contrario imprime None

### otro ejemplo
texto = "No atendemos los lunes"

buscar = re.search(r"lunes|martes", texto) # Busca la palabra "lunes" en el texto
print(buscar)

### Ejercicios

'''
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, 
que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) 
y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", 
pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.

'''
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
          print("Ok")
    else:
          print("La dirección de email es incorrecta")

'''
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". 
Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", 
debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla

'''
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")

'''
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos 
y cuatro numéricos a continuación (ejemplo: XX1234). 
Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".

'''
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

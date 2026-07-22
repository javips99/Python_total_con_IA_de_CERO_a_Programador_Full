
### Manejo de errores en Python

# try: Permite ejecutar un bloque de código y capturar excepciones si ocurren. (obligatorio)
# except: Permite manejar la excepción capturada y ejecutar un bloque de código alternativo. (obligatorio)
# else: Permite ejecutar un bloque de código si no ocurre ninguna excepción. (opcional)
# finally: Permite ejecutar un bloque de código que se ejecutará siempre, sin importar si ocurrió una excepción o no. (opcional)


def al_cuadrado():
    try: # El codigo que puede fallar
        numero = int(input("Ingrese un número: "))
        resultado = numero ** 2
        print(f"El cuadrado de {numero} es {resultado}.")
        
    except ValueError: # El codigo que debe ejecutarse si falla el bloque try
        print("Error: Debe ingresar un número válido.")

    else:# El codigo que se ejecuta si no hay errores
        print("¡Operación exitosa!")

    finally:# El codigo que se ejecuta siempre, haya error o no
        print("Gracias por usar el programa.")

al_cuadrado()

##### otro ejemplo

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except:
            print("Error: Debe ingresar un número válido.")
        else:
            print("Ingresastes el número: ", numero)
            break
        print("Intentelo de nuevo.")

pedir_numero()

### Ejercicios

'''
Implementa para la siguiente función suma(), 
un manejador de errores simple que ante cualquier error, 
imprima en pantalla el mensaje: "Error inesperado". 
En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.

'''
"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")


'''
Implementa para la siguiente función cociente(), un manejador de errores:
Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: 
"Los argumentos a ingresar deben ser números"
Si se generara una división por cero (error del tipo ZeroDivisionError), 
el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"
En caso que no se produzca un error, 
deberá limitarse a imprimir el resultado del cociente (división) 
entre los dos números entregados como argumento.
Ejemplo de resolución:

'''
def cociente(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


'''
Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), 
mostrar en pantalla el mensaje: "El archivo no fue encontrado"
En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
En todos los casos, al finalizar, imprimir: "Finalizando ejecución"

'''

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
        print("Abriendo exitosamente")
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")

abrir_archivo("archivo_inexistente.txt")

from numeros import generador_perfumeria, generador_farmacia, generador_cosmeticos
from numeros import mostrar_turno

turnos_perfumeria = generador_perfumeria()
turnos_farmacia = generador_farmacia()
turnos_cosmeticos = generador_cosmeticos()

while True:
    print("Bienvenido a la consola de turnos")
    print("Por favor, seleccione una opción:")
    print("1. Perfumería")
    print("2. Farmacia")
    print("3. Cosméticos")
    print("4. Salir")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        mostrar_turno(turnos_perfumeria)
    elif opcion == "2":
        mostrar_turno(turnos_farmacia)
    elif opcion == "3":
        mostrar_turno(turnos_cosmeticos)
    elif opcion == "4":
        print("Gracias por usar la consola de turnos. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
# mi programa

nombre = input("¿Cual es tu nombre? ")

ingresos_usuario = input("¿Cuales son tus ingresos? ")
ingresos_usuario = float (ingresos_usuario)

comision = round(13 * ingresos_usuario / 100,2)


print(f"El trabajador {nombre} ha obtenido unos ingresos de {ingresos_usuario} y unas comisones de {comision}")

# solucion profesor

nombre = input("Dime tu nombre: ")
ventas = int(input("Por favor, ingresa el monto total de tus ventas: "))

comisiones = round(ventas * 13 / 100, 2)

print(f"El empleado {nombre} tiene una comisión de {comisiones}$")
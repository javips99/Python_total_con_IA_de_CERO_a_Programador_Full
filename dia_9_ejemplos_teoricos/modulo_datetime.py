
from datetime import datetime, date, time

mi_hora = time(17, 35, 10)
print("Mi hora es:", mi_hora)

mi_dia = date(2026, 10, 3)
print("Mi día es:", mi_dia)

momento_actual = datetime.now()
fecha_formateada = momento_actual.strftime("%d/%m/%Y a las %H:%M")
print("La fecha y hora actual es:", fecha_formateada)

# Calcular la diferencia entre dos fechas
fecha1 = date(1986, 10, 3)
fecha2 = date(2026, 7, 23)
diferencia = fecha2 - fecha1
print("La diferencia entre las fechas es:", diferencia.days, "días")


### Ejercicios

'''
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero de 1999

'''
mi_fecha = date(1999, 2, 3)

'''
Crea un objeto en la variable hoy que siempre almacene la fecha actual cuando sea invocada

'''
hoy = date.today()

'''
En una variable llamada minutos, almacena únicamente los minutos de la hora actual.
Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43

'''

minutos = datetime.now().minute
print("Los minutos son:", minutos)
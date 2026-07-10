
nombre = input("Introduce tu nombre ")

print("Tu nombre es: " + nombre)

palabra1 = "Hola"

palabra2 = " Python"

print(palabra1 + palabra2)

nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print(nombrecompleto)

num_entero = 25
print(type(num_entero))

num_decimal = 17.25
print(type(num_decimal))

num1 = 7.5
num2 = 2.5

print(type(num1 + num2))
precio = 19.99
impuesto = precio * 0.16
print(round(impuesto, 2)) # redondear decimales


# conversiones

num1 = 5.8

print(num1)
print(type(num1))

num2 = int (num1)

print(num2)
print(type(num2))


num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))
print(type(num1))
print(type(num2))



### formatear cadenas, tenemos 2 formas:
    # función format

color_coche = "rojo"
matricula = "3585 GHD"
print("Mi coche es {} y la matrícula es {}".format(color_coche,matricula))

    
    # Cadenas literales (f-strings)
x = 10
y = 5
print(f"Mis números son {x} y {y} y la suma es {x+y}")

puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


# redondeo
print(97/7)
print(round(98/7,2))

valor = 10.676767
print(round(valor))

# Calcula la raíz cuadrada de 5, 
# y muestra en pantalla el resultado redondeado con 4 posiciones decimales.


raiz = 5**0.5
print(round(raiz,4))

num1 = 13.87

print(round(num1))
print(int(num1))
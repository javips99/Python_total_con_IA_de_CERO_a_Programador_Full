
# desempaquetar tuplas

lista_cafe = [("capuchino", 2.3), ("expreso", 1.20), ("moka", 1.9)]

for cafe, precio in lista_cafe:
    print(cafe, precio)

###

lista_cafe = [("capuchino", 2.3), ("expreso", 1.20), ("moka", 1.9)]

def encontrar_cafe_mas_caro(lista):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
            
    return(cafe_mas_caro, precio_mayor)

cafe, precio = encontrar_cafe_mas_caro(lista_cafe)
print(f"El cafe mas caro es {cafe} y su precio es {precio} €")

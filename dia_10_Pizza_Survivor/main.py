import math

import pygame
import random

# Initialize Pygame

pygame.init()

# Crear la ventana del juego
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")  # Título de la ventana
icono = pygame.image.load("pizza.png")  # Cargar el ícono del juego
pygame.display.set_icon(icono)  # Establecer el ícono de la ventana

# Fondo de la pantalla
fondo = pygame.image.load("fondo.png")  # Cargar la imagen de fondo
fondo = pygame.transform.scale(fondo, (800, 600))  # Escalar la imagen de fondo al tamaño de la ventana


# Repartidor de pizzas
repartidor_img = pygame.image.load("repartidor.png")  # Cargar la imagen del repartidor
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100)) # Tamaño del repartidor
repartidor_x = 368  # Posición inicial en el eje X
repartidor_y = 440  
repartidor_cambio_x = 0  # Cambio en la posición del repartidor en el eje X
repartidor_cambio_y = 0  
velocidad_repartidor = 1  # Velocidad del movimiento repartidor

pizza_img = pygame.image.load("pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (32, 32))


# Perro enemigo
perro_img = pygame.image.load("perro.png")  # Cargar la imagen del perro
perro_img = pygame.transform.scale(perro_img, (54, 64))
velocidad_perro = 0.4 

def crear_perro():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        return {"x": random.randint(0, 800 - perro_img.get_width()), "y": 0}
    if borde == "abajo":
        return {"x": random.randint(0, 800 - perro_img.get_width()), "y": 600 - perro_img.get_height()}
    if borde == "izquierda":
        return {"x": 0, "y": random.randint(0, 600 - perro_img.get_height())}

    return {"x": 800 - perro_img.get_width(), "y": random.randint(0, 600 - perro_img.get_height())}


perros = [crear_perro()]

pizzas = []
ultimo_disparo = pygame.time.get_ticks()
intervalo_disparo = 1000
velocidad_pizza = 0.6
ultimo_spawn_perro = pygame.time.get_ticks()
intervalo_spawn_perro = 3000


def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))  # Dibujar el repartidor en la pantalla

def perro(x, y):
    pantalla.blit(perro_img, (x, y))  

def pizza(x, y):
    pantalla.blit(pizza_img, (x, y))

def obtener_perro_mas_cercano(origen_x, origen_y, lista_perros):
    if not lista_perros:
        return None

    return min(
        lista_perros,
        key=lambda perro_actual: math.hypot(
            origen_x - perro_actual["x"],
            origen_y - perro_actual["y"],
        ),
    )

def lanzar_pizza(origen_x, origen_y, objetivo):
    origen_centro_x = origen_x + repartidor_img.get_width() / 2
    origen_centro_y = origen_y + repartidor_img.get_height() / 2
    objetivo_centro_x = objetivo["x"] + perro_img.get_width() / 2
    objetivo_centro_y = objetivo["y"] + perro_img.get_height() / 2

    dx = objetivo_centro_x - origen_centro_x
    dy = objetivo_centro_y - origen_centro_y
    distancia = math.hypot(dx, dy)

    if distancia == 0:
        return

    pizzas.append(
        {
            "x": origen_centro_x - pizza_img.get_width() / 2,
            "y": origen_centro_y - pizza_img.get_height() / 2,
            "dx": (dx / distancia) * velocidad_pizza,
            "dy": (dy / distancia) * velocidad_pizza,
        }
    )

def actualizar_pizzas():
    pizzas_a_eliminar = []

    for pizza_actual in pizzas:
        pizza_actual["x"] += pizza_actual["dx"]
        pizza_actual["y"] += pizza_actual["dy"]

        if (
            pizza_actual["x"] < -pizza_img.get_width()
            or pizza_actual["x"] > 800
            or pizza_actual["y"] < -pizza_img.get_height()
            or pizza_actual["y"] > 600
        ):
            pizzas_a_eliminar.append(pizza_actual)

    for pizza_actual in pizzas_a_eliminar:
        pizzas.remove(pizza_actual)

def detectar_colisiones():
    global perros, pizzas

    pizzas_sobrevivientes = []
    perros_sobrevivientes = list(perros)

    for pizza_actual in pizzas:
        pizza_chocada = False

        for perro_actual in perros_sobrevivientes[:]: # Iterar sobre una copia de la lista para evitar problemas al eliminar elementos
            dx = pizza_actual["x"] + pizza_img.get_width() / 2 - (perro_actual["x"] + perro_img.get_width() / 2)
            dy = pizza_actual["y"] + pizza_img.get_height() / 2 - (perro_actual["y"] + perro_img.get_height() / 2)
            distancia = math.hypot(dx, dy)

            if distancia < 30:
                perros_sobrevivientes.remove(perro_actual)
                pizza_chocada = True
                break

        if not pizza_chocada:
            pizzas_sobrevivientes.append(pizza_actual)

    perros = perros_sobrevivientes
    pizzas = pizzas_sobrevivientes
    

# Loop del juego
se_ejecuta = True

while se_ejecuta:
    ahora = pygame.time.get_ticks()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:  
            if evento.key == pygame.K_LEFT:  
                repartidor_cambio_x = -velocidad_repartidor  
            if evento.key == pygame.K_RIGHT:  
                repartidor_cambio_x = velocidad_repartidor  
            if evento.key == pygame.K_UP:  
                repartidor_cambio_y = -velocidad_repartidor  
            if evento.key == pygame.K_DOWN:  
                repartidor_cambio_y = velocidad_repartidor  

        if evento.type == pygame.KEYUP:  # Si se suelta una tecla
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):  
                repartidor_cambio_x = 0  
            if evento.key in (pygame.K_UP, pygame.K_DOWN):  
                repartidor_cambio_y = 0  

    # Actualizar la posición
    repartidor_x += repartidor_cambio_x   
    repartidor_y += repartidor_cambio_y

    # Limitar el movimiento a la izquierda y derecha
    if repartidor_x < 0:  
        repartidor_x = 0
    elif repartidor_x > 736: 
        repartidor_x = 736

    # Limitar el movimiento hacia arriba y abajo     
    if repartidor_y < 0:  
        repartidor_y = 0
    elif repartidor_y > 500:  
        repartidor_y = 500

    if ahora - ultimo_spawn_perro >= intervalo_spawn_perro:
        perros.append(crear_perro())
        ultimo_spawn_perro = ahora

    if ahora - ultimo_disparo >= intervalo_disparo:
        perro_mas_cercano = obtener_perro_mas_cercano(repartidor_x, repartidor_y, perros)
        if perro_mas_cercano is not None:
            lanzar_pizza(repartidor_x, repartidor_y, perro_mas_cercano)
        ultimo_disparo = ahora

    # Movimiento del perro
    for perro_actual in perros:
        dx = repartidor_x - perro_actual["x"]
        dy = repartidor_y - perro_actual["y"]
        distancia = (dx**2 + dy**2) ** 0.5

        if distancia > 0:
            perro_actual["x"] += (dx / distancia) * velocidad_perro
            perro_actual["y"] += (dy / distancia) * velocidad_perro

    actualizar_pizzas()
    detectar_colisiones()

    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla
    repartidor(repartidor_x, repartidor_y)  # Dibujar el repartidor en la pantalla

    for perro_actual in perros:
        perro(perro_actual["x"], perro_actual["y"])

    for pizza_actual in pizzas:
        pizza(pizza_actual["x"], pizza_actual["y"])


    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

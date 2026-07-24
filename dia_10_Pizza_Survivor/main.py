import math
import pygame
import random

from interface import (
    dibujar_cronometro,
    dibujar_pantalla_fin,
    dibujar_puntuaje,
    dibujar_vidas,
)
from resources import cargar_imagenes, cargar_sonidos, iniciar_musica_fondo
from repartidor import Repartidor
from perro import Perro
from pizza import Pizza

# Initialize Pygame

pygame.init()

try:
    pygame.mixer.init()
    sonido_disponible = True
except pygame.error:
    sonido_disponible = False

# Crear la ventana del juego
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pizza Survivor")  # Título de la ventana
imagenes = cargar_imagenes()
pygame.display.set_icon(imagenes["icono"])  # Establecer el ícono de la ventana

fondo = imagenes["fondo"]
corazon_img = imagenes["corazon"]

sonidos = cargar_sonidos(sonido_disponible)
sonido_disparo = sonidos["disparo"]
sonido_golpe = sonidos["golpe"]
sonido_vida_perdida = sonidos["vida_perdida"]

if sonido_disponible:
    iniciar_musica_fondo()


# Repartidor de pizzas
repartidor_img = imagenes["repartidor"]
velocidad_repartidor = 0.8  # Velocidad del movimiento repartidor

pizza_img = imagenes["pizza"]


# Perro enemigo
perro_img = imagenes["perro"]
velocidad_perro = 0.2 

# Puntuaje y tiempo
puntuaje = 0
fuente = pygame.font.Font(None, 36)  # Fuente para mostrar el puntuaje
tiempo_inicio = pygame.time.get_ticks()  # Tiempo de inicio del juego
tiempo_final = None
estado_juego = "jugando"



def crear_perro():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        return Perro(random.randint(0, 800 - perro_img.get_width()), 0, perro_img, velocidad_perro)
    if borde == "abajo":
        return Perro(random.randint(0, 800 - perro_img.get_width()), 600 - perro_img.get_height(), perro_img, velocidad_perro)
    if borde == "izquierda":
        return Perro(0, random.randint(0, 600 - perro_img.get_height()), perro_img, velocidad_perro)

    return Perro(800 - perro_img.get_width(), random.randint(0, 600 - perro_img.get_height()), perro_img, velocidad_perro)


perros = [crear_perro()]

pizzas = []
ultimo_disparo = pygame.time.get_ticks()
intervalo_disparo = 2500
velocidad_pizza = 0.6
ultimo_spawn_perro = pygame.time.get_ticks()
intervalo_spawn_perro = 2000
vidas_repartidor = 3
inmunidad_hasta = 0
intervalo_inmunidad = 1000
intervalo_parpadeo = 150


repartidor = Repartidor(368, 440, repartidor_img, velocidad_repartidor)


def reproducir_sonido(sonido):
    if sonido_disponible and sonido is not None:
        sonido.play()

def obtener_tiempo_sobrevivido(ahora):
    if tiempo_final is not None:
        return tiempo_final - tiempo_inicio

    return ahora - tiempo_inicio

def obtener_perro_mas_cercano(origen_x, origen_y, lista_perros):
    if not lista_perros:
        return None

    return min(
        lista_perros,
        key=lambda perro_actual: math.hypot(origen_x - perro_actual.x, origen_y - perro_actual.y),
    )

def lanzar_pizza(origen_x, origen_y, objetivo):
    origen_centro_x = origen_x + repartidor_img.get_width() / 2
    origen_centro_y = origen_y + repartidor_img.get_height() / 2
    objetivo_centro_x = objetivo.centro_x()
    objetivo_centro_y = objetivo.centro_y()

    dx = objetivo_centro_x - origen_centro_x
    dy = objetivo_centro_y - origen_centro_y
    distancia = math.hypot(dx, dy)

    if distancia == 0:
        return

    pizzas.append(
        Pizza(
            origen_centro_x - pizza_img.get_width() / 2,
            origen_centro_y - pizza_img.get_height() / 2,
            pizza_img,
            velocidad_pizza,
            dx / distancia,
            dy / distancia,
        )
    )

    reproducir_sonido(sonido_disparo)

def actualizar_pizzas():
    pizzas_a_eliminar = []

    for pizza_actual in pizzas:
        pizza_actual.mover()

        if pizza_actual.fuera_de_pantalla():
            pizzas_a_eliminar.append(pizza_actual)

    for pizza_actual in pizzas_a_eliminar:
        pizzas.remove(pizza_actual)

def detectar_colisiones():
    global perros, pizzas, puntuaje

    pizzas_sobrevivientes = []
    perros_sobrevivientes = list(perros)

    for pizza_actual in pizzas:
        pizza_chocada = False

        for perro_actual in perros_sobrevivientes[:]: # Iterar sobre una copia de la lista para evitar problemas al eliminar elementos
            dx = pizza_actual.centro_x() - perro_actual.centro_x()
            dy = pizza_actual.centro_y() - perro_actual.centro_y()
            distancia = math.hypot(dx, dy)

            if distancia < 30:
                puntuaje += 10
                perros_sobrevivientes.remove(perro_actual)
                reproducir_sonido(sonido_golpe)
                pizza_chocada = True
                break

        if not pizza_chocada:
            pizzas_sobrevivientes.append(pizza_actual)

    perros = perros_sobrevivientes
    pizzas = pizzas_sobrevivientes

def detectar_colisiones_con_repartidor(ahora):
    global perros, vidas_repartidor, inmunidad_hasta, estado_juego, tiempo_final

    perros_sobrevivientes = []
    repartidor_centro_x = repartidor.centro_x()
    repartidor_centro_y = repartidor.centro_y()
    radio_repartidor = 30
    radio_perro = 22

    for perro_actual in perros:
        perro_centro_x = perro_actual.centro_x()
        perro_centro_y = perro_actual.centro_y()
        dx = perro_centro_x - repartidor_centro_x
        dy = perro_centro_y - repartidor_centro_y
        distancia = math.hypot(dx, dy)

        if distancia < radio_repartidor + radio_perro:
            perro_actual.revertir_posicion()

            if ahora >= inmunidad_hasta:
                vidas_repartidor = max(0, vidas_repartidor - 1)
                inmunidad_hasta = ahora + intervalo_inmunidad
                reproducir_sonido(sonido_vida_perdida)

                if vidas_repartidor == 0 and estado_juego != "terminado":
                    estado_juego = "terminado"
                    tiempo_final = ahora
                    if sonido_disponible:
                        pygame.mixer.music.stop()
                continue

        perros_sobrevivientes.append(perro_actual)

    perros = perros_sobrevivientes

def actualizar_juego(ahora):
    global ultimo_spawn_perro, ultimo_disparo

    if ahora - ultimo_spawn_perro >= intervalo_spawn_perro:
        perros.append(crear_perro())
        ultimo_spawn_perro = ahora

    if ahora - ultimo_disparo >= intervalo_disparo:
        perro_mas_cercano = obtener_perro_mas_cercano(repartidor.x, repartidor.y, perros)
        if perro_mas_cercano is not None:
            lanzar_pizza(repartidor.x, repartidor.y, perro_mas_cercano)
        ultimo_disparo = ahora

    for perro_actual in perros:
        perro_actual.guardar_posicion_anterior()
        perro_actual.mover_hacia(repartidor.x, repartidor.y)

    actualizar_pizzas()
    detectar_colisiones()
    detectar_colisiones_con_repartidor(ahora)


def dibujar_juego(ahora):
    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla

    if ahora >= inmunidad_hasta or (ahora // intervalo_parpadeo) % 2 == 0:
        repartidor.dibujar(pantalla)

    for perro_actual in perros:
        perro_actual.dibujar(pantalla)

    for pizza_actual in pizzas:
        pizza_actual.dibujar(pantalla)

    dibujar_vidas(pantalla, corazon_img, vidas_repartidor)
    dibujar_puntuaje(pantalla, fuente, puntuaje)
    dibujar_cronometro(pantalla, fuente, obtener_tiempo_sobrevivido(ahora))


# Loop del juego
se_ejecuta = True

while se_ejecuta:
    ahora = pygame.time.get_ticks()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:  
            if evento.key == pygame.K_LEFT:  
                repartidor.cambio_x = -velocidad_repartidor  
            if evento.key == pygame.K_RIGHT:  
                repartidor.cambio_x = velocidad_repartidor  
            if evento.key == pygame.K_UP:  
                repartidor.cambio_y = -velocidad_repartidor  
            if evento.key == pygame.K_DOWN:  
                repartidor.cambio_y = velocidad_repartidor  

        if evento.type == pygame.KEYUP:  # Si se suelta una tecla
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):  
                repartidor.cambio_x = 0  
            if evento.key in (pygame.K_UP, pygame.K_DOWN):  
                repartidor.cambio_y = 0  

    if estado_juego == "jugando":
        repartidor.mover()
        repartidor.limitar_movimiento()

        actualizar_juego(ahora)
        dibujar_juego(ahora)
    else:
        tiempo_fin = tiempo_final if tiempo_final is not None else pygame.time.get_ticks()
        dibujar_pantalla_fin(pantalla, fondo, fuente, puntuaje, obtener_tiempo_sobrevivido(tiempo_fin))

    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

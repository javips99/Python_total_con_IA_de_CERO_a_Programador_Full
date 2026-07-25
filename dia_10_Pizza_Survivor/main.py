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
from gato import Gato
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


# Enemigos
perro_img = imagenes["perro"]
gato_img = imagenes["gato"]
velocidad_perro = 0.12
velocidad_gato = 0.28

# Puntuaje y tiempo
puntuaje = 0
fuente = pygame.font.Font(None, 36)  # Fuente para mostrar el puntuaje
tiempo_inicio = pygame.time.get_ticks()  # Tiempo de inicio del juego
tiempo_final = None
estado_juego = "jugando"



def crear_enemigo():
    borde = random.choice(["arriba", "abajo", "izquierda", "derecha"])
    tipo_enemigo = random.choices(["perro", "gato"], weights=[0.7, 0.3])[0]

    if tipo_enemigo == "gato":
        imagen = gato_img
        velocidad = velocidad_gato
        clase = Gato
    else:
        imagen = perro_img
        velocidad = velocidad_perro
        clase = Perro

    if borde == "arriba":
        return clase(random.randint(0, 800 - imagen.get_width()), 0, imagen, velocidad)
    if borde == "abajo":
        return clase(random.randint(0, 800 - imagen.get_width()), 600 - imagen.get_height(), imagen, velocidad)
    if borde == "izquierda":
        return clase(0, random.randint(0, 600 - imagen.get_height()), imagen, velocidad)

    return clase(800 - imagen.get_width(), random.randint(0, 600 - imagen.get_height()), imagen, velocidad)


enemigos = [crear_enemigo()]

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

def obtener_enemigo_mas_cercano(origen_x, origen_y, lista_enemigos):
    if not lista_enemigos:
        return None

    return min(
        lista_enemigos,
        key=lambda enemigo_actual: math.hypot(origen_x - enemigo_actual.x, origen_y - enemigo_actual.y),
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
    global enemigos, pizzas, puntuaje

    pizzas_sobrevivientes = []
    enemigos_sobrevivientes = list(enemigos)

    for pizza_actual in pizzas:
        pizza_chocada = False

        for enemigo_actual in enemigos_sobrevivientes[:]:
            dx = pizza_actual.centro_x() - enemigo_actual.centro_x()
            dy = pizza_actual.centro_y() - enemigo_actual.centro_y()
            distancia = math.hypot(dx, dy)

            if distancia < 30:
                puntuaje += 10
                enemigos_sobrevivientes.remove(enemigo_actual)
                reproducir_sonido(sonido_golpe)
                pizza_chocada = True
                break

        if not pizza_chocada:
            pizzas_sobrevivientes.append(pizza_actual)

    enemigos = enemigos_sobrevivientes
    pizzas = pizzas_sobrevivientes

def detectar_colisiones_con_repartidor(ahora):
    global enemigos, vidas_repartidor, inmunidad_hasta, estado_juego, tiempo_final

    enemigos_sobrevivientes = []
    repartidor_centro_x = repartidor.centro_x()
    repartidor_centro_y = repartidor.centro_y()
    radio_repartidor = 30
    radio_enemigo = 22

    for enemigo_actual in enemigos:
        enemigo_centro_x = enemigo_actual.centro_x()
        enemigo_centro_y = enemigo_actual.centro_y()
        dx = enemigo_centro_x - repartidor_centro_x
        dy = enemigo_centro_y - repartidor_centro_y
        distancia = math.hypot(dx, dy)

        if distancia < radio_repartidor + radio_enemigo:
            enemigo_actual.revertir_posicion()

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

        enemigos_sobrevivientes.append(enemigo_actual)

    enemigos = enemigos_sobrevivientes

def actualizar_juego(ahora):
    global ultimo_spawn_perro, ultimo_disparo

    if ahora - ultimo_spawn_perro >= intervalo_spawn_perro:
        enemigos.append(crear_enemigo())
        ultimo_spawn_perro = ahora

    if ahora - ultimo_disparo >= intervalo_disparo:
        enemigo_mas_cercano = obtener_enemigo_mas_cercano(repartidor.x, repartidor.y, enemigos)
        if enemigo_mas_cercano is not None:
            lanzar_pizza(repartidor.x, repartidor.y, enemigo_mas_cercano)
        ultimo_disparo = ahora

    for enemigo_actual in enemigos:
        enemigo_actual.guardar_posicion_anterior()
        enemigo_actual.mover_hacia(repartidor.x, repartidor.y)

    actualizar_pizzas()
    detectar_colisiones()
    detectar_colisiones_con_repartidor(ahora)


def dibujar_juego(ahora):
    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla

    if ahora >= inmunidad_hasta or (ahora // intervalo_parpadeo) % 2 == 0:
        repartidor.dibujar(pantalla)

    for enemigo_actual in enemigos:
        enemigo_actual.dibujar(pantalla)

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

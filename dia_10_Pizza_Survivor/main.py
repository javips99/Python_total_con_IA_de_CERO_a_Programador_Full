import math

import pygame
import random

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
icono = pygame.image.load("pizza.png")  # Cargar el ícono del juego
pygame.display.set_icon(icono)  # Establecer el ícono de la ventana

# Fondo de la pantalla
fondo = pygame.image.load("fondo.png")  # Cargar la imagen de fondo
fondo = pygame.transform.scale(fondo, (800, 600))  # Escalar la imagen de fondo al tamaño de la ventana

corazon_img = pygame.image.load("corazon.png")
corazon_img = pygame.transform.scale(corazon_img, (32, 32))

# Sonidos

if sonido_disponible:
    pygame.mixer.music.load("MusicaFondo.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    sonido_disparo = pygame.mixer.Sound("disparo.mp3")
    sonido_golpe = pygame.mixer.Sound("golpe.mp3")
    sonido_vida_perdida = pygame.mixer.Sound("vida_perdida.mp3")

    sonido_disparo.set_volume(0.8)
    sonido_golpe.set_volume(0.8)
    sonido_vida_perdida.set_volume(0.8)
else:
    sonido_disparo = None
    sonido_golpe = None
    sonido_vida_perdida = None


# Repartidor de pizzas
repartidor_img = pygame.image.load("repartidor.png")  # Cargar la imagen del repartidor
repartidor_img = pygame.transform.scale(repartidor_img, (64, 100)) # Tamaño del repartidor
repartidor_x = 368  # Posición inicial en el eje X
repartidor_y = 440  
repartidor_cambio_x = 0  # Cambio en la posición del repartidor en el eje X
repartidor_cambio_y = 0  
velocidad_repartidor = 0.8  # Velocidad del movimiento repartidor

pizza_img = pygame.image.load("pizza.png")
pizza_img = pygame.transform.scale(pizza_img, (32, 32))


# Perro enemigo
perro_img = pygame.image.load("perro.png")  # Cargar la imagen del perro
perro_img = pygame.transform.scale(perro_img, (54, 64))
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
        return {"x": random.randint(0, 800 - perro_img.get_width()), "y": 0}
    if borde == "abajo":
        return {"x": random.randint(0, 800 - perro_img.get_width()), "y": 600 - perro_img.get_height()}
    if borde == "izquierda":
        return {"x": 0, "y": random.randint(0, 600 - perro_img.get_height())}

    return {"x": 800 - perro_img.get_width(), "y": random.randint(0, 600 - perro_img.get_height())}


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


def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))  # Dibujar el repartidor en la pantalla

def perro(x, y):
    pantalla.blit(perro_img, (x, y))  

def pizza(x, y):
    pantalla.blit(pizza_img, (x, y))

def corazon(x, y):
    pantalla.blit(corazon_img, (x, y))

def reproducir_sonido(sonido):
    if sonido_disponible and sonido is not None:
        sonido.play()

def formatear_tiempo(tiempo_ms):
    segundos_totales = tiempo_ms // 1000
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    return f"{minutos}:{segundos:02d}"

def obtener_tiempo_sobrevivido(ahora):
    if tiempo_final is not None:
        return tiempo_final - tiempo_inicio

    return ahora - tiempo_inicio

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

    reproducir_sonido(sonido_disparo)

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
    global perros, pizzas, puntuaje

    pizzas_sobrevivientes = []
    perros_sobrevivientes = list(perros)

    for pizza_actual in pizzas:
        pizza_chocada = False

        for perro_actual in perros_sobrevivientes[:]: # Iterar sobre una copia de la lista para evitar problemas al eliminar elementos
            dx = pizza_actual["x"] + pizza_img.get_width() / 2 - (perro_actual["x"] + perro_img.get_width() / 2)
            dy = pizza_actual["y"] + pizza_img.get_height() / 2 - (perro_actual["y"] + perro_img.get_height() / 2)
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
    repartidor_centro_x = repartidor_x + repartidor_img.get_width() / 2
    repartidor_centro_y = repartidor_y + repartidor_img.get_height() / 2
    radio_repartidor = 30
    radio_perro = 22

    for perro_actual in perros:
        perro_centro_x = perro_actual["x"] + perro_img.get_width() / 2
        perro_centro_y = perro_actual["y"] + perro_img.get_height() / 2
        dx = perro_centro_x - repartidor_centro_x
        dy = perro_centro_y - repartidor_centro_y
        distancia = math.hypot(dx, dy)

        if distancia < radio_repartidor + radio_perro:
            perro_actual["x"] = perro_actual.get("prev_x", perro_actual["x"])
            perro_actual["y"] = perro_actual.get("prev_y", perro_actual["y"])

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

def dibujar_vidas():
    for indice in range(vidas_repartidor):
        corazon(10 + indice * 36, 10)
    
def dibujar_puntuaje():
    texto_puntuaje = fuente.render(f"Puntuaje: {puntuaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntuaje, (600, 10))

def dibujar_cronometro(ahora):
    tiempo_sobrevivido = obtener_tiempo_sobrevivido(ahora)
    texto_cronometro = fuente.render(f"Tiempo: {formatear_tiempo(tiempo_sobrevivido)}", True, (255, 255, 255))
    rectangulo = texto_cronometro.get_rect(midtop=(400, 10))
    pantalla.blit(texto_cronometro, rectangulo)

def dibujar_pantalla_fin():
    texto_game_over = pygame.font.Font(None, 88).render("GAME OVER", True, (255, 0, 0))
    texto_game_over_rect = texto_game_over.get_rect(center=(400, 220))

    texto_puntaje_final = fuente.render(f"Puntaje final: {puntuaje}", True, (255, 255, 255))
    texto_puntaje_final_rect = texto_puntaje_final.get_rect(center=(400, 350))

    tiempo_sobrevivido = obtener_tiempo_sobrevivido(tiempo_final if tiempo_final is not None else pygame.time.get_ticks())
    texto_tiempo_final = fuente.render(f"Tiempo sobrevivido: {formatear_tiempo(tiempo_sobrevivido)}", True, (255, 255, 255))
    texto_tiempo_final_rect = texto_tiempo_final.get_rect(center=(400, 390))

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(texto_game_over, texto_game_over_rect)
    pantalla.blit(texto_puntaje_final, texto_puntaje_final_rect)
    pantalla.blit(texto_tiempo_final, texto_tiempo_final_rect)


def actualizar_juego(ahora):
    global repartidor_x, repartidor_y, ultimo_spawn_perro, ultimo_disparo

    if ahora - ultimo_spawn_perro >= intervalo_spawn_perro:
        perros.append(crear_perro())
        ultimo_spawn_perro = ahora

    if ahora - ultimo_disparo >= intervalo_disparo:
        perro_mas_cercano = obtener_perro_mas_cercano(repartidor_x, repartidor_y, perros)
        if perro_mas_cercano is not None:
            lanzar_pizza(repartidor_x, repartidor_y, perro_mas_cercano)
        ultimo_disparo = ahora

    for perro_actual in perros:
        perro_actual["prev_x"] = perro_actual["x"]
        perro_actual["prev_y"] = perro_actual["y"]
        dx = repartidor_x - perro_actual["x"]
        dy = repartidor_y - perro_actual["y"]
        distancia = (dx**2 + dy**2) ** 0.5

        if distancia > 0:
            perro_actual["x"] += (dx / distancia) * velocidad_perro
            perro_actual["y"] += (dy / distancia) * velocidad_perro

    actualizar_pizzas()
    detectar_colisiones()
    detectar_colisiones_con_repartidor(ahora)


def dibujar_juego(ahora):
    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla

    if ahora >= inmunidad_hasta or (ahora // intervalo_parpadeo) % 2 == 0:
        repartidor(repartidor_x, repartidor_y)

    for perro_actual in perros:
        perro(perro_actual["x"], perro_actual["y"])

    for pizza_actual in pizzas:
        pizza(pizza_actual["x"], pizza_actual["y"])

    dibujar_vidas()
    dibujar_puntuaje()
    dibujar_cronometro(ahora)


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

    if estado_juego == "jugando":
        repartidor_x += repartidor_cambio_x   
        repartidor_y += repartidor_cambio_y

        if repartidor_x < 0:  
            repartidor_x = 0
        elif repartidor_x > 736: 
            repartidor_x = 736

        if repartidor_y < 0:  
            repartidor_y = 0
        elif repartidor_y > 500:  
            repartidor_y = 500

        actualizar_juego(ahora)
        dibujar_juego(ahora)
    else:
        dibujar_pantalla_fin()

    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

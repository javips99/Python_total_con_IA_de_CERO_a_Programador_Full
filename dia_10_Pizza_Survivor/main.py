import pygame


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

def repartidor(x, y):
    pantalla.blit(repartidor_img, (x, y))  # Dibujar el repartidor en la pantalla


# Loop del juego
se_ejecuta = True

while se_ejecuta:

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

    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla
    repartidor(repartidor_x, repartidor_y)  # Dibujar el repartidor en la pantalla
    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

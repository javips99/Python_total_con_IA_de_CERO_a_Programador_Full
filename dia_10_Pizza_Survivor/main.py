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


# Loop del juego
se_ejecuta = True

while se_ejecuta:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

    pantalla.blit(fondo, (0, 0))  # Dibujar el fondo en la pantalla

    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

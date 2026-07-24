import pygame


# Initialize Pygame

pygame.init()

# Crear la ventana del juego
pantalla = pygame.display.set_mode((800, 600))

# Loop del juego
se_ejecuta = True

while se_ejecuta:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            se_ejecuta = False

    pantalla.fill((230, 220, 240))  # Modificar el color de fondo de la pantalla 

    # Actualizar la pantalla
    pygame.display.update() 

pygame.quit()  # Cerrar Pygame

"""Funciones de interfaz visual del juego: HUD y pantalla final."""

import pygame


def formatear_tiempo(tiempo_ms):
    # Convierte milisegundos a formato M:SS para mostrar el cronómetro.
    segundos_totales = tiempo_ms // 1000
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    return f"{minutos}:{segundos:02d}"


def dibujar_vidas(pantalla, corazon_img, vidas_repartidor):
    for indice in range(vidas_repartidor):
        pantalla.blit(corazon_img, (10 + indice * 36, 10))


def dibujar_puntuaje(pantalla, fuente, puntuaje):
    texto_puntuaje = fuente.render(f"Puntuaje: {puntuaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntuaje, (600, 10))


def dibujar_cronometro(pantalla, fuente, tiempo_ms):
    texto_cronometro = fuente.render(
        f"Tiempo: {formatear_tiempo(tiempo_ms)}",
        True,
        (255, 255, 255),
    )
    rectangulo = texto_cronometro.get_rect(midtop=(400, 10))
    pantalla.blit(texto_cronometro, rectangulo)


def dibujar_pantalla_fin(pantalla, fondo, fuente, puntuaje, tiempo_ms):
    # Pantalla final simple con el resultado de la partida.
    texto_game_over = pygame.font.Font(None, 88).render("GAME OVER", True, (255, 0, 0))
    texto_game_over_rect = texto_game_over.get_rect(center=(400, 220))

    texto_puntaje_final = fuente.render(f"Puntaje final: {puntuaje}", True, (255, 255, 255))
    texto_puntaje_final_rect = texto_puntaje_final.get_rect(center=(400, 350))

    texto_tiempo_final = fuente.render(
        f"Tiempo sobrevivido: {formatear_tiempo(tiempo_ms)}",
        True,
        (255, 255, 255),
    )
    texto_tiempo_final_rect = texto_tiempo_final.get_rect(center=(400, 390))

    pantalla.blit(fondo, (0, 0))
    pantalla.blit(texto_game_over, texto_game_over_rect)
    pantalla.blit(texto_puntaje_final, texto_puntaje_final_rect)
    pantalla.blit(texto_tiempo_final, texto_tiempo_final_rect)
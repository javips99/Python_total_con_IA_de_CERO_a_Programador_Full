"""Carga centralizada de imágenes y sonidos del juego."""

from pathlib import Path

import pygame

BASE_DIR = Path(__file__).resolve().parent
RECURSOS_DIR = BASE_DIR / "recursos"


def obtener_ruta_recurso(nombre_archivo):
    """Devuelve la ruta absoluta del recurso, buscando primero en la carpeta del juego y luego en recursos/."""
    rutas_posibles = [BASE_DIR / nombre_archivo, RECURSOS_DIR / nombre_archivo]

    for ruta in rutas_posibles:
        if ruta.exists():
            return ruta

    return RECURSOS_DIR / nombre_archivo


def cargar_imagen(ruta, tamaño=None):
    # Carga una imagen y, si hace falta, la escala al tamaño pedido.
    imagen = pygame.image.load(str(obtener_ruta_recurso(ruta)))
    if tamaño is not None:
        imagen = pygame.transform.scale(imagen, tamaño)
    return imagen


def cargar_imagenes():
    # Agrupa todos los recursos visuales para que main.py no los cargue uno a uno.
    return {
        "icono": cargar_imagen("pizza.png"),
        "fondo": cargar_imagen("fondo.png", (800, 600)),
        "corazon": cargar_imagen("corazon.png", (32, 32)),
        "repartidor": cargar_imagen("repartidor.png", (64, 100)),
        "pizza": cargar_imagen("pizza.png", (32, 32)),
        "perro": cargar_imagen("perro.png", (54, 64)),
    }


def cargar_sonido(ruta, volumen):
    # Carga un efecto de sonido y aplica su volumen.
    sonido = pygame.mixer.Sound(str(obtener_ruta_recurso(ruta)))
    sonido.set_volume(volumen)
    return sonido


def cargar_sonidos(sonido_disponible):
    # Si el mixer no está disponible, devolvemos sonidos vacíos para evitar errores.
    if not sonido_disponible:
        return {
            "disparo": None,
            "golpe": None,
            "vida_perdida": None,
        }

    return {
        "disparo": cargar_sonido("disparo.mp3", 0.8),
        "golpe": cargar_sonido("golpe.mp3", 0.8),
        "vida_perdida": cargar_sonido("vida_perdida.mp3", 0.8),
    }


def iniciar_musica_fondo(volumen=0.2):
    # Inicia la música del juego en bucle.
    pygame.mixer.music.load(str(obtener_ruta_recurso("MusicaFondo.mp3")))
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(-1)
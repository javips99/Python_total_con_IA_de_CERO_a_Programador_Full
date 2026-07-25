"""Enemigo concreto del juego: el gato."""

from enemigo import Enemigo


class Gato(Enemigo):
    def __init__(self, x, y, imagen, velocidad):
        # El gato solo define su aspecto y su velocidad.
        super().__init__(x, y, imagen, velocidad)

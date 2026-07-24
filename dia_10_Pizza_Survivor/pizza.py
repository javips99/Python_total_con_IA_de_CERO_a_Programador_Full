"""Proyectil concreto del juego: la pizza."""

from proyectil import Proyectil


class Pizza(Proyectil):
    def __init__(self, x, y, imagen, velocidad, dx, dy):
        # La pizza reutiliza el comportamiento base del proyectil sin añadir más reglas.
        super().__init__(x, y, imagen, velocidad, dx, dy)
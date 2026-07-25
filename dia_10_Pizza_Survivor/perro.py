"""Enemigo concreto del juego: el perro."""

from enemigo import Enemigo


class Perro(Enemigo):
	def __init__(self, x, y, imagen, velocidad):
		# El perro solo define su aspecto y su velocidad.
		super().__init__(x, y, imagen, velocidad)

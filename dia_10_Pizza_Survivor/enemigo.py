"""Base común para enemigos que persiguen al jugador."""

import math

class Enemigo:
	def __init__(self, x, y, imagen, velocidad):
		# Posición, imagen y velocidad son los datos comunes a todos los enemigos.
		self.x = x
		self.y = y
		self.imagen = imagen
		self.velocidad = velocidad
		self.prev_x = x
		self.prev_y = y

	def centro_x(self):
		return self.x + self.imagen.get_width() / 2

	def centro_y(self):
		return self.y + self.imagen.get_height() / 2

	def guardar_posicion_anterior(self):
		# Guarda la posición previa para poder deshacer el movimiento si hay colisión.
		self.prev_x = self.x
		self.prev_y = self.y

	def revertir_posicion(self):
		self.x = self.prev_x
		self.y = self.prev_y

	def mover_hacia(self, objetivo_x, objetivo_y):
		# Mueve al enemigo en línea recta hacia el objetivo.
		dx = objetivo_x - self.x
		dy = objetivo_y - self.y
		distancia = math.hypot(dx, dy)

		if distancia > 0:
			self.x += (dx / distancia) * self.velocidad
			self.y += (dy / distancia) * self.velocidad

	def dibujar(self, pantalla):
		# Dibuja el sprite del enemigo en la pantalla.
		pantalla.blit(self.imagen, (self.x, self.y))

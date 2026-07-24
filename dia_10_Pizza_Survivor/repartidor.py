"""Jugador controlado por teclado."""


class Repartidor:
	def __init__(self, x, y, imagen, velocidad):
		# El repartidor guarda posición, sprite y velocidad base.
		self.x = x
		self.y = y
		self.imagen = imagen
		self.velocidad = velocidad
		self.cambio_x = 0
		self.cambio_y = 0

	def centro_x(self):
		return self.x + self.imagen.get_width() / 2

	def centro_y(self):
		return self.y + self.imagen.get_height() / 2

	def mover(self):
		# Aplica el movimiento acumulado por teclado.
		self.x += self.cambio_x
		self.y += self.cambio_y

	def limitar_movimiento(self):
		# Evita que el jugador salga de la ventana.
		if self.x < 0:
			self.x = 0
		elif self.x > 736:
			self.x = 736

		if self.y < 0:
			self.y = 0
		elif self.y > 500:
			self.y = 500

	def dibujar(self, pantalla):
		# Dibuja el personaje en pantalla.
		pantalla.blit(self.imagen, (self.x, self.y))

"""Base común para proyectiles lanzados por el jugador."""


class Proyectil:
    def __init__(self, x, y, imagen, velocidad, dx, dy):
		# dx y dy representan la dirección normalizada del disparo.
        self.x = x
        self.y = y
        self.imagen = imagen
        self.velocidad = velocidad
        self.dx = dx
        self.dy = dy

    def centro_x(self):
        return self.x + self.imagen.get_width() / 2

    def centro_y(self):
        return self.y + self.imagen.get_height() / 2

    def mover(self):
		# Avanza manteniendo dirección fija y velocidad constante.
        self.x += self.dx * self.velocidad
        self.y += self.dy * self.velocidad

    def fuera_de_pantalla(self):
		# Se elimina cuando deja de ser visible.
        return (
            self.x < -self.imagen.get_width()
            or self.x > 800
            or self.y < -self.imagen.get_height()
            or self.y > 600
        )

    def dibujar(self, pantalla):
		# Render del proyectil.
        pantalla.blit(self.imagen, (self.x, self.y))
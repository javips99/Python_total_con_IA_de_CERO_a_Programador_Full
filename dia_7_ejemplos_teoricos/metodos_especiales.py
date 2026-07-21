
class CD:
    def __init__(self, titulo, artista, numero_canciones):
        self.titulo = titulo
        self.artista = artista
        self.numero_canciones = numero_canciones

    def __str__(self):
        return f"Título del álbum: {self.titulo} Artista: {self.artista}, {self.numero_canciones} canciones"

    def __len__(self):
        return self.numero_canciones
    
    def __del__(self):
        print(f"El CD '{self.titulo}' de {self.artista} ha sido eliminado.")

cd1 = CD("The Dark Side of the Moon", "Pink Floyd", 10)

print(cd1)  # Salida: Título del álbum: The Dark Side of the Moon Artista: Pink Floyd, 10 canciones
print(len(cd1))  # Salida: 10
del cd1  # Salida: El CD 'The Dark Side of the Moon' de 'Pink Floyd' ha sido eliminado.

### Ejercicios

'''
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, 
devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

'''
Dada la clase Libro, implementa el método especial __len__ 
para que cada vez que se ejecute la función len() sobre el mismo, 
devuelva el número de páginas como número entero.

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__ (self):
        return self.cantidad_paginas


'''
Dada la clase Libro, implementa el método especial __del__ 
para que el usuario sea informado con el mensaje "Libro eliminado", 
mostrándolo en pantalla cada vez que el libro se elimine.

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
from bs4 import BeautifulSoup
import requests

# Lista para almacenar los títulos de libros con 4 o 5 estrellas
titulos_altas_valoraciones = []

# Iterar por las 50 páginas del catálogo
for pagina in range(1, 51):

    # Crear URL para cada página
    url_pagina = f"https://books.toscrape.com/catalogue/page-{pagina}.html"

    # Realizar la petición HTTP a la página
    resultado = requests.get(url_pagina)
    sopa = BeautifulSoup(resultado.text, "lxml")

    # Seleccionar todos los elementos de los libros en la página
    libros = sopa.select(".product_pod")

    # Evaluar cada libro de la página
    for libro in libros:

        # Verificar si el libro tiene 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # Extraer y guardar el título en la lista
            titulo_libro = libro.select("h3 a")[0]["title"]
            titulos_altas_valoraciones.append(titulo_libro)

# Imprimir los títulos capturados al finalizar el recorrido
for titulo in titulos_altas_valoraciones:
    print(titulo)

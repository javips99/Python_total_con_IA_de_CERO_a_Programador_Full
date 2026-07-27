# Pagina para practicar Scraping: https://fede-garay.vercel.app/

# Scraping sirve para obtener informacion de paginas web, extraer datos y hacer que un programa interactue con una pagina web.

# Importar las librerías necesarias
from bs4 import BeautifulSoup
import requests 

# Realizar la petición HTTP para obtener la página web
resultado = requests.get("https://fede-garay.vercel.app/")

# Parsear el HTML de la página con BeautifulSoup usando el analizador 'lxml'
sopa = BeautifulSoup(resultado.text, "lxml")

# Extraer e imprimir la etiqueta del título de la página
print(sopa.select("title"))

# Recorrer e imprimir el texto de cada título (h3) en la sección #videos
for titulo in sopa.select("#videos h3"):
    print(titulo.get_text())

# Recorrer e imprimir el texto de cada título (h3) en la sección #interviews
for titulo in sopa.select("#interviews h3"):
    print(titulo.get_text())

# Extraer e imprimir los enlaces ('href') de los elementos <a> en #videos
for etiqueta in sopa.select("#videos a"):
    print(etiqueta["href"])

# Seleccionar la primera imagen (<img>) encontrada en la página
imagen = sopa.select("img")[0]

# Construir la URL completa de la imagen combinando el dominio base y la ruta del atributo 'src'
url_imagen = "https://fede-garay.vercel.app/" + imagen["src"]
print(url_imagen)

# Descargar los datos binarios de la imagen mediante una petición GET
respuesta_imagen = requests.get(url_imagen).content

# Crear y abrir un archivo en modo escritura binaria ('wb') para guardar la imagen localmente
foto = open("imagen.png", "wb")
foto.write(respuesta_imagen)
foto.close()
print("Imagen descargada exitosamente")


 
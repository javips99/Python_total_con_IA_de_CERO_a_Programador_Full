from bs4 import BeautifulSoup
import requests

url = "https://x.com/NASA"

respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "lxml")
print(soup.prettify())



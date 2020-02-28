import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.hendyla.com/casas.html")
soup = BeautifulSoup(page.content,"html.parser")
casas = soup.find_all("article", class_ ="product-item clasificado")
primera_casa = casas[0] #se saca la primera casa de la pagina pero aqui se podria poner cualquier indice dentro del rango
primer_precio = primera_casa.find_all("div", class_ ="precio left")[0].p.get_text()
primer_precio = primer_precio[primer_precio.find("Gs.")+4:] #para borrar el espacio y el Gs. 
descripcion = primera_casa.select("div.desc a")[0].get_text() #selecciona todas las "a" que tengan la clase desc dentro del div
print(descripcion)
print("Precio: ",primer_precio)
#print(len(descripcion))
url_publicacion = primera_casa.select("div.desc a")[0].get("href") 
print("Url de la publicacion: ",url_publicacion) #esta es la url de la pagina
imagen = primera_casa.select("figure.img img")[0].get("src") #la url de la imagen
print("Url de la imagen: ",imagen)

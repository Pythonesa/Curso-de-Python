from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import os

def descargar_imagen(url):
    imagen = None
    with urlopen(url) as img:
        imagen = img.read()
        
    if not imagen:
        raise Exception(f"No se pudo descargar la imagen {url}")
    
    archivo = os.path.basename(url)
    with open(archivo, 'wb') as f:
        f.write(imagen)
        print(f"Se descargó la imagen {f.name}")
        
urls = [
    "https://i.pinimg.com/originals/a2/6c/4b/a26c4b485716a585073da2af4328a8cd.jpg",
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg",
    "https://www.shutterstock.com/image-photo/smart-phone-python-logo-interpreted-260nw-1618686154.jpg",
    "https://c8.alamy.com/comp/2PGD2FD/poland-07th-mar-2023-in-this-photo-illustration-a-python-logo-seen-displayed-on-a-smartphone-credit-sopa-images-limitedalamy-live-news-2PGD2FD.jpg",
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    "https://www.python.org/static/community_logos/python-powered-w-200x80.png",
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    "https://cdn5.vectorstock.com/i/1000x1000/25/54/python-programming-language-vector-11282554.jpg"
]

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(descargar_imagen, urls)
    
print("Se descargaron todas las imágenes!")
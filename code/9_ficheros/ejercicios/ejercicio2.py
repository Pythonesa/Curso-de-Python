'''
    Crear un programa que dado el path y nombre de un archivo 
    devuelva la cantidad de líneas, palabras y bytes que hay en el fichero. 
    Número de bytes de un string llamado texto: len(texto.enconde('utf-8))
'''
import re

path = 'ficheros/test1'
#path = input("Ingrese el path y nombre del archivo: ")

lineas = 0
palabras = 0
bytes_ = 0

with open(path) as fichero:
    for linea in fichero:
        lineas += 1
        palabras += len(re.findall('\w+', linea))
        bytes_ += len(linea.encode('utf-8'))

print(f'El fichero tiene {lineas} líneas, {palabras} palabras y {bytes_} bytes.')
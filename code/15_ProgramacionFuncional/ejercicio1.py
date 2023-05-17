'''Crear una lista de diccionarios que contengan el nombre y edad de varias personas.
   Sumar las edades de todas las personas de la lista.
   Mostrar el promedio de las edades.
'''

from functools import reduce

personas = [
    {"Nombre:": "Patonesa", "Edad": 1},
    {"Nombre:": "Pepe", "Edad": 36},
    {"Nombre:": "María", "Edad": 35},
    {"Nombre:": "José", "Edad": 46},
    {"Nombre:": "Pedro", "Edad": 63}
]

suma_edades = reduce(lambda suma, persona: suma + persona["Edad"], personas, 0)
promedio_edades = suma_edades / len(personas)
print(f'La edad promedio es de {promedio_edades}')
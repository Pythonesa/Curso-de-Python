'''Añadir al ejercicio anterior el sexo de la persona (F o M).
   Permitir que el usuario ingrese el sexo de quienes quiere conocer la media de edades.
   Mostrar el promedio del sexo seleccionado.
'''

from functools import reduce

personas = [
    {"Nombre:": "Patonesa", "Edad": 1, "Sexo": "F"},
    {"Nombre:": "Pepe", "Edad": 36, "Sexo": "M"},
    {"Nombre:": "María", "Edad": 35, "Sexo": "F"},
    {"Nombre:": "José", "Edad": 46, "Sexo": "M"},
    {"Nombre:": "Pedro", "Edad": 63, "Sexo": "M"}
]

sexo = input("Ingrese el sexo de las personas para las que quiere el promedio 'F' o 'M': ")

personas_filtradas = list(filter(lambda persona: persona["Sexo"] == sexo.upper(), personas))
suma_edades = reduce(lambda suma, persona: suma + persona["Edad"], personas_filtradas, 0)
promedio_edades = suma_edades / len(personas_filtradas)
print(f'La edad promedio es de {promedio_edades}')
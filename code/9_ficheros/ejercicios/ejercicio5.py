'''
    Cree un programa que muestre las palabras que han salido en el ahorcado 
    (leyendo el archivo de logs del ejercicio anterior) 
    y cuantas veces han sido adivinadas y falladas.
'''

import re

#Leemos las lineas del archivo:
lineas = []

with open('ficheros/estadisticas_ahorcado') as fichero:
    lineas = fichero.readlines()

#Obtenemos las palabras y generamos las estadisticas:
palabras = []
estadisticas = []

for linea in lineas:
    palabras_linea = re.findall('\w+', linea)
    if palabras_linea[0] not in palabras:
        palabras.append(palabras_linea[0])
        if palabras_linea[1] == 'fue':
            estadisticas.append([palabras_linea[0], 1, 0])
        else:
            estadisticas.append([palabras_linea[0], 0, 1])
    else:
        if palabras_linea[1] == 'fue':
            for estadistica in estadisticas:
                if palabras_linea[0] == estadistica[0]:
                    estadistica[1] += 1
        else:
            for estadistica in estadisticas:
                if palabras_linea[0] == estadistica[0]:
                    estadistica[2] += 1

#Mostramos las estadísticas:
for estadistica in estadisticas:
    print(f'La palabra {estadistica[0]} ha sido adivinada {estadistica[1]} y fallada {estadistica[2]}.')
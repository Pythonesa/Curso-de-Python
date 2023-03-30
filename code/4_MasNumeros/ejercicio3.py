'''
    Calcular el volumen de una esfera a partir del radio ingresado por el usuario, mostrar el resultado con 2 cifras decimales.
'''
import math

print('Vamos a calcular el volumen de una esfera!')
radio = float(input("Ingresa el valor del radio de la esfera: "))

volumen = round(3 / 4 * math.pi * radio ** 3 , 2)

print(f'El volumen de una esfera de radio {radio} es {volumen}')
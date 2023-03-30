'''
    Calcular el área de un círculo a partir del radio ingresado por el usuario, 
    mostrar el resultado con 2 cifras decimales.
'''

import math # podemos utilizar esta librería para utilizar math.pi (o bien, pueden crear una constante PI o variable pi y asignarle el valor de pi)
#tengan en cuenta que los valores van a variar un poco dependiendo de los decimales que le pongan a pi

print('Vamos a calcular el área de un círculo!')
radio = float(input('Ingresa el valor del radio del círculo: '))

area = round(math.pi * radio ** 2 , 2)

print(f'El área de un círculo con radio {radio} es de {area}')

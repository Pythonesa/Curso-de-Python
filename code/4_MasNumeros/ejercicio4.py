'''
    Calcular el área de un triángulo a partir de la base y altura que ingrese el usuario, 
    mostrar el resultado con 2 cifras decimales.
'''

print('Vamos a calcular el área de un triángulo!')
base = float(input('Ingresa el valor de la base del triángulo: '))
altura = float(input('Ingresa el valor de la altura del triángulo: '))

area = round((base * altura) / 2 , 2)

print(f'El área de un triángulo con una base de {base} y una altura de {altura} es de {area}.')
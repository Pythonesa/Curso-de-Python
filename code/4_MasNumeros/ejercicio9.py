'''
    Una persona debe tomar medio litro de agua cada hora, 
    pedir al usuario que ingrese la cantidad de horas 
    y mostrar cuantos litros de agua debe tomar.
'''

print("Calcula cuantos litros de agua debes tomar!")

horas = float(input("Ingresa la cantidad de horas: "))

cant_agua = horas * 0.5

print(f'En {horas} horas debes tomar {cant_agua} litros de agua.')
'''
    Pedir al usuario que ingrese una cantidad de horas, minutos y segundos; 
    mostrar la cantidad de milisegundos.
'''

print("Calculemos los milisegundos!")

horas = float(input("Ingrese la cantidad de horas: "))
minutos = float(input("Ingrese la cantidad de minutos: "))
segundos = float(input("Ingrese la cantidad de segundos: "))

milisegundos = horas * 3.6e+6 + minutos * 60000 + segundos * 1000

print(f'La cantidad de segundos equivalentes al tiempo ingresado es de {milisegundos}')
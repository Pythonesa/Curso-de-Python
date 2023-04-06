# Crear un programa donde el usuario pueda jugar piedra, papel o tijera contra la computadora.

import random

def obtener_opcion():
    opciones = ['piedra', 'papel', 'tijera']
    opcion = random.choice(opciones)
    return opcion

opcion_usuario = input("Ingrese piedra, papel o tijera: ")
opcion_computadora = obtener_opcion()
print(f'La elección de la computadora es {opcion_computadora}.')

match opcion_usuario:
    case 'piedra':
        if opcion_computadora == 'piedra':
            print("Empate!")
        elif opcion_computadora == 'papel':
            print("La computadora gana!")
        else:
            print("Ganaste!")
    case 'papel':
        if opcion_computadora == 'papel':
            print("Empate!")
        elif opcion_computadora == 'tijera':
            print("La computadora gana!")
        else:
            print("Ganaste!")
    case 'tijera':
        if opcion_computadora == 'tijera':
            print("Empate!")
        elif opcion_computadora == 'piedra':
            print("La computadora gana!")
        else:
            print("Ganaste!")
    case _:
        print("La opción ingresada no es válida.")
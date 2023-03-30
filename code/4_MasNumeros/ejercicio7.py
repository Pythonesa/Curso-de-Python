'''
    En un juego, un jugador tira el dado y se mueve por el tablero 2 veces el número que le sale. 
    Pedir al jugador el número de su casilla de inicio y 
    mostrar el resultado del dado (del 1 al 6) y el número de casillero donde quedará al moverse.
'''

import random

print("Bienvenid@ al juego sin sentido de tablero sin tablero!")

casilla_inicial = int(input("Ingrese el número de su casilla actual: "))

dado = random.randint(1,6)
movimiento = dado * 2
casilla_actual = casilla_inicial + movimiento

print(f'Lanzas el dado y sacas {dado}, avanzas {movimiento} casillas hasta la casilla {casilla_actual}.')
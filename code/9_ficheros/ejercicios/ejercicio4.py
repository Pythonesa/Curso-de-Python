'''
    Agregue al juego del ahorcado (que está disponible en github de cuando lo hicimos en stream) 
    un log que deberá añadir por cada palabra que se adivine o no algo así: "Palabra fue adivinada/no adivinada".
'''

import ahorcado

palabra, adivinada = ahorcado.jugar()

if adivinada:
    texto = f'{palabra} fue adivinada.'
else:
    texto = f'{palabra} no fue adivinada.'

with open('ficheros/estadisticas_ahorcado', 'a') as fichero:
    fichero.write(texto + '\n')

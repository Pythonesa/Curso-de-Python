'''
    Juego del ahorcado, donde se debe adivinar una palabra antes de morir ahorcado (6 intentos)!
'''

import random

def get_palabra():
    '''
        Devuelve una palabra elegida aleatoriamente de una lista.
    '''
    palabras = ['cocodrilo','mariposa','felicidad','cereza','globo','paraguas','maquillaje','cangrejo','espejo',
                'elefante', 'tijeras', 'botella','computadora','guitarra','pizza','arcoiris','camion','pantalla',
                'gorila','estrella','lapiz','zanahoria','cafe','volcan','silla','calabaza','gato','telescopio',
                'helado','reloj','martillo','aire','diamante','pastel','brocoli','chimenea','limon','pavo','almohada',
                'pescado','tractor','fresa','serpiente','nube','cama','diente','botas','cactus','periodico','ballena']
    return random.choice(palabras)

def print_ahorcado(intentos):
    '''
        Dibuja el ahorcado según la cantidad de intentos restantes.
    '''
    match intentos:
        case 6:
            print(' ________     ')
            print('|        |    ')
            print('|             ')
            print('|             ')
            print('|             ')
            print('|____________ ')
        case 5:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|             ')
            print('|             ')
            print('|____________ ')
        case 4:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|        |    ')
            print('|             ')
            print('|____________ ')
        case 3:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|       /|    ')
            print('|             ')
            print('|____________ ')
        case 2:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|       /|\   ')
            print('|             ')
            print('|____________ ')
        case 1:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|       /|\   ')
            print('|       /     ')
            print('|____________ ')
        case _:
            print(' ________     ')
            print('|        |    ')
            print('|        O    ')
            print('|       /|\   ')
            print('|       / \   ')
            print('|____________ ')

def jugar():
    '''
        Devuelve la palabra y un bool que indica si se adivino la palabra.
    '''
    palabra = get_palabra()
    intentos_restantes = 6
    palabra_mostrada = ['_'] * len(palabra)
    letras_usadas = []
    adivinada = False

    while intentos_restantes > 0:
        print_ahorcado(intentos_restantes)
        cadena_mostrada = ' '.join(palabra_mostrada)
        print(f'Tu palabra: {cadena_mostrada}')
        print(f'Letras utilizadas: {letras_usadas}')
        letra = input("Ingresa una letra: ").lower()
        #Verificar si la letra ya fue usada:
        if letra in letras_usadas:
            print("Ya ingresaste esa letra, intenta con otra.")
        #Verificar si la letra está en la palabra:
        elif letra in palabra:
            print("La letra existe en la palabra!")
            letras_usadas.append(letra)
            #Actualizar la palabra mostrada:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_mostrada[i] = letra
            #Verificar si adivino la palabra:
            if '_' not in palabra_mostrada:
                print(f'¡Felicidades! Adivinaste la palabra {palabra}.')
                adivinada = True
                break
        else:
            print("La letra no se encuentra en la palabra.")
            letras_usadas.append(letra)
            intentos_restantes -= 1
        if intentos_restantes == 0:
            print_ahorcado(intentos_restantes)
            print(f'Perdiste, la palabra era {palabra}')
    
    return palabra, adivinada


if __name__ == '__main__':
    _, _ = jugar()
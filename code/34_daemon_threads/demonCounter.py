from threading import Thread
import time


def mostrar_contador():
    contador = 0
    while True:
        contador += 1
        time.sleep(1)
        print(f'Llevamos esperando {contador} segudo/s...')


t = Thread(target=mostrar_contador, daemon=True)
t.start()

answer = input('Presione cualquier tecla para salir...\n')
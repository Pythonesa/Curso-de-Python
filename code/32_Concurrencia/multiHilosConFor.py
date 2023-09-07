from time import sleep, perf_counter
from threading import Thread

def tarea():
    print("Iniciando tarea...")
    sleep(1)
    print("Tarea terminada")
    
tiempo_inicial = perf_counter()

hilos = []
for n in range(1, 10000):
    hilo = Thread(target=tarea)
    hilos.append(hilo)
    hilo.start()
    
for h in hilos:
    h.join()

tiempo_final = perf_counter()

print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial: 0.3f} segundos")
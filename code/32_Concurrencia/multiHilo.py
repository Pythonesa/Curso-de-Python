from time import sleep, perf_counter
from threading import Thread

def tarea():
    print("Iniciando tarea...")
    sleep(1)
    print("Tarea terminada")
    
tiempo_inicial = perf_counter()

t1 = Thread(target=tarea)
t2 = Thread(target=tarea)
t3 = Thread(target=tarea)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

tiempo_final = perf_counter()

print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial: 0.3f} segundos")
from time import sleep, perf_counter

def tarea():
    print("Iniciando tarea...")
    sleep(1)
    print("Tarea terminada")
    
tiempo_inicial = perf_counter()

tarea()
tarea()
tarea()

tiempo_final = perf_counter()

print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial: 0.2f} segundos")
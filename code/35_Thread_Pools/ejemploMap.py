from concurrent.futures import ThreadPoolExecutor
from time import sleep

def tarea(id):
    print(f"Empieza la tarea {id}")
    sleep(2)
    return f"Termina la tarea {id}"

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(tarea, range(1, 6))
    
    for result in results:
        print(result)    
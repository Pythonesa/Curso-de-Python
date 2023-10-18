from concurrent.futures import ThreadPoolExecutor
from time import sleep

def tarea(id):
    print(f"Empieza la tarea {id}")
    sleep(2)
    return f"Termina la tarea {id}"

with ThreadPoolExecutor(max_workers=2) as executor:
    f1 = executor.submit(tarea, 1)
    f2 = executor.submit(tarea, 2)
    f3 = executor.submit(tarea, 3)
    f4 = executor.submit(tarea, 4)
    f5 = executor.submit(tarea, 5)
    
    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())
    print(f5.result())
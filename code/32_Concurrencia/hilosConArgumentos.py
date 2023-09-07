from time import sleep, perf_counter
from threading import Thread

def suma(num1, num2):
    sleep(1)
    suma = num1 + num2
    print(f"La suma de {num1} + {num2} es: {suma}")
    
tiempo_inicial = perf_counter()

# suma(100, 200)
# suma(200, 300)
# suma(300, 400)
# suma(400, 500)

# tiempo_final = perf_counter()

# print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial: 0.3f} segundos")

t1 = Thread(target=suma, args=(100, 200))
t2 = Thread(target=suma, args=(200, 300))
t3 = Thread(target=suma, args=(300, 400))
t4 = Thread(target=suma, args=(400, 500))
t5 = Thread(target=suma, args=(500, 600))
t6 = Thread(target=suma, args=(600, 700))
t7 = Thread(target=suma, args=(700, 800))
t8 = Thread(target=suma, args=(800, 900))
t9 = Thread(target=suma, args=(900, 1000))
t10 = Thread(target=suma, args=(1000, 1100))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()

tiempo_final = perf_counter()

print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicial: 0.3f} segundos")

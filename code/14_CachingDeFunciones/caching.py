'''
caché -> almacenamiento de resultados previos para posterior reutilización.
- Reduce tiempo de respuesta.
Si tenemos una función con un parámetro y la llamamos con un valor
y luego volvemos a llamarla con ese mismo valor,
si utilizamos caching de funciones podemos reutilizar lo retornado la primera vez.

caché miss -> si el resultado no ha sido calculado anteriormente se calcula y almacena.
caché hit -> si ya ha sido calculado el resultado está en caché y lo reutilizamos.

Usos principales:
- funciones intensivas de cálculo.
- los argumentos de llamada no son muy dispares y se van a repetir bastante.
- mejor tiempo de respuesta pagando con un incremento en uso de memoria.
'''

from time import time
from functools import lru_cache

#Calculo de números primos:
# def obtener_es_primo(num):
#     for n in range(2, num):
#         if num % n == 0:
#             return False
#     return True

# print(obtener_es_primo(6))
# print(obtener_es_primo(13))

# tic = time()
# print(obtener_es_primo(25565479))
# print(time() - tic)

# tic = time()
# print(obtener_es_primo(25565479))
# print(time() - tic)

#Caché de funciones con diccionario:
# cache_Diccionario = {}
# def obtener_es_primo_diccionario(num):
#     if num not in cache_Diccionario:
#         cache_Diccionario[num] = True
#         for n in range(2, num):
#             if num % n == 0:
#                 cache_Diccionario[num] = False
#                 break
#     return cache_Diccionario[num]

# tic = time()
# print(obtener_es_primo_diccionario(25565479))
# print(time() - tic)

# tic = time()
# print(obtener_es_primo_diccionario(25565479))
# print(time() - tic)

# Caché de funciones con @lru_cache (más sofisticado y sin modificar la función):
# lru_cache es un decorador de la librería estándar functools.
# como parámetro al decorador le pasamos el número máximo de valores a almacenar.

@lru_cache(maxsize=64)
def obtener_es_primo_cache(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

tic = time()
print(obtener_es_primo_cache(25565479))
print(time() - tic)

tic = time()
print(obtener_es_primo_cache(25565479))
print(time() - tic)
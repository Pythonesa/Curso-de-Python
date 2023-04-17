"""
Crear un programa que dado un número n ingresado por el usuario
imprima n números de la sucesión de fibonacci 
(implementar una función recursiva para fibonacci y 
otra con un for utilizando un range para cada número).
"""

numero = int(input("Ingrese la cantidad de números para la secuencia: "))

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(numero):
    print(fibonacci(n))
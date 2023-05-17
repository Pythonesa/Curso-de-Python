#Filtrado de números pares con filter:
lista = [5, 2, 3, 7, 8, 12]
pares = filter(lambda num: num % 2 == 0, lista)
print(list(pares))
print(next(pares))
print(next(pares))
print(next(pares))
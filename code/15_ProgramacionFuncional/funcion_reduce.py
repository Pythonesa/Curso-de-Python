from functools import reduce
from operator import add, mul

lista = [1, 2, 3, 4]

suma = reduce(add, lista)
multiplicacion = reduce(mul, lista)

print(suma)
print(multiplicacion)

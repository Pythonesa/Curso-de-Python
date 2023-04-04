# Pida al usuario un número entero (n) y muestre el resultado de n + nn + nnn.

numero = input('Ingrese un número entero: ')
numero2 = int(numero * 2)
numero3 = int(numero * 3)
numero = int(numero)
suma = numero + numero2 + numero3

print(f'El resultado de {numero} + {numero2} + {numero3} es {suma}.')
# Pida al usuario dos números y muestre el resultado de su división, división entera y resto.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

division = num1 / num2
division_entera = num1 // num2
resto = num1 % num2

print(f'El resultado de dividir {num1} entre {num2} es {division}, también podemos decir que es {int(division_entera)} con un resto de {int(resto)}')
# Pida al usuario una palabra y muestre cuantas vocales tiene (utilizando for).

palabra = input("Ingrese una palabra: ")

vocales = 0

for letra in palabra:
    if letra in 'aeiou':
        vocales += 1

print(f'La palabra {palabra} tiene {vocales} vocales.')
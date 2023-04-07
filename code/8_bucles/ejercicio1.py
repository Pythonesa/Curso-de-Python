#Escribir un programa que imprima todos los múltiplos de un número menores a un valor dado (utilizando while).

multiplo = int(input("Ingrese el múltiplo que desea: "))
tope = int(input("Ingrese el número tope: "))

numero = 1

while numero < tope:
    if numero % multiplo == 0:
        print(numero)
    numero += 1
else:
    print(f'Esos son los múltiplos de {multiplo} menores al número {tope}.')
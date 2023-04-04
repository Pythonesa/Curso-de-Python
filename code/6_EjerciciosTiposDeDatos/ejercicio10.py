'''
    Pida al usuario que ingrese un número entero (n) y 
    muestre en pantalla el resultado de n por 5 elevado al número de dígitos de n.
'''

numero = input("Ingrese un número entero: ")
digitos = len(numero)
numero = int(numero)

print((numero * 5) ** digitos)
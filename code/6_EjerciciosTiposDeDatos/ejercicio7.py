'''
    Pida al usuario que ingrese una palabra y 
    muestre el resultado de multiplicar el número total de caracteres por el número total de vocales.
'''

palabra = input("Ingrese una palabra: ")

caracteres = len(palabra)

vocales = palabra.count('a') + palabra.count('e') + palabra.count('i') + palabra.count('o') + palabra.count('u')

multiplicacion = caracteres * vocales

print(f'Su palabra tiene {caracteres} caracteres y {vocales} vocales, el resultado de multiplicar ambos valores es {multiplicacion}')
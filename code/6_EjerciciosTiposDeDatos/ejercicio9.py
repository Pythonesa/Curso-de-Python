'''
    Pida al usuario que ingrese un texto y 
    muestre en pantalla el texto sin el primer y el último caracter.
'''

texto = input("Ingrese un texto: ")

largo = len(texto)

print(texto[1:largo-1])
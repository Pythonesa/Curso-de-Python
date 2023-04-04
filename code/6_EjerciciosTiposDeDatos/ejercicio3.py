# Pida al usuario que ingrese un texto y muestre cuantas caracteres y palabras contiene.
import re

texto = input("Ingrese un texto: ")

caracteres = len(texto)

lista_palabras = re.findall("\w+" , texto)

palabras = len(lista_palabras)

print(f'El texto ingresado tiene {caracteres} caracteres y {palabras} palabras.')
# Pida al usuario que ingrese el código de un caracter unicode y muestrelo.

codigo = input("Ingrese el código de un caracter unicode: ")
caracter = chr(int(codigo, 16))

print(caracter)
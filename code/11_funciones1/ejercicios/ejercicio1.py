'''
Pide al usuario que ingrese su nombre 
y crea una función que devuelva una lista con las letras del nombre en mayúsculas
y muestralas por pantalla una por línea.
'''


nombre = input('Ingresa tu nombre: ')


def obtener_letras(nombre: str) -> list:
    letras = []
    for letra in nombre:
        letras.append(letra.upper())
    return letras


letras = obtener_letras(nombre)

for letra in letras:
    print(letra)
#int (enteros):
entero = 5
print(f'La variable entero tiene un valor {entero} y es de tipo {type(entero)}')
binario = 0b100
print(f'La variable binario tiene un valor {binario} y es de tipo {type(binario)}')
hexadecimal = 0x17
print(f'La variable hexadecimal tiene un valor {hexadecimal} y es de tipo {type(hexadecimal)}')
octal = 0o720
print(f'La variable octal tiene un valor {octal} y es de tipo {type(octal)}')
#bool (booleanos)
activo = True
print(f'La variable activo tiene un valor {activo} y es de tipo {type(activo)} ')
disponible = False
print(f'La variable disponible tiene un valor {disponible} y es de tipo {type(disponible)}')
#float (números con coma flotante):
flotante = 4.7
print(f'La variable flotante tiene un valor {flotante} y es de tipo {type(flotante)}')
#complex (complejos)
complejo = 2j
print(f'La variable complejo tiene un valor {complejo} y es de tipo {type(complejo)}' )

#string (cadena de texto):
cadena = "hola! soy un texto..."
print(f'La variable cadena tiene un valor {cadena} y es de tipo {type(cadena)}')
#list (lista):
compras = ['limones', 'agua', 'papel de cocina']
print(f'La variable compras tiene una lista de valores {compras} y es de tipo {type(compras)}')
#set (como las listas pero los valores deben de ser unicos, no pueden repetirse):
conjunto_enteros = set([1, 2, 3])
print(f'La variable conjunto_enteros tiene un conjunto de valores unicos {conjunto_enteros} y es de tipo {type(conjunto_enteros)}')
#frozenset (como los sets pero los valores no pueden ser modificados durante la ejecución)
conjunto_letras = frozenset(['i','j','k'])
print(f'La variable conjunto_letras tiene un conjunto de valores inmutables {conjunto_letras} y es de tipo {type(conjunto_letras)}')
#tuple (tuplas - como las listas, pero los valores no pueden ser modificados durante la ejecución):
tupla_letras = ('a','b','c')
print(f'La variable tupla_letras tiene una lista de valores inmutables {tupla_letras} y es de tipo {type(tupla_letras)}')
#diccionarios:
info_alumno = {
    "Nombre": "Pepe",
    "Edad": "35"
}
print(f'La variable info_alumno tiene claves-valores {info_alumno} y es de tipo {type(info_alumno)}')

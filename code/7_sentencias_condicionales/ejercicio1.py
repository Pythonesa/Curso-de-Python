'''
Pedir al usuario una edad humana y 
mostrar el equivalente en años perro y años gato. 
(Años perro: 15 años para el primer año, +9 para el segundo, +5 para los demás. 
Años gato: 15 años para el primero, +9 para el segundo, +4 para los demás.)
'''

anios_humanos = int(input("Ingrese la edad humana: "))

match anios_humanos:
    case 1:
        anios_perro = 15
        anios_gato = 15
    case 2:
        anios_perro = 15 + 9
        anios_gato = 15 + 9
    case _:
        anios_perro = 15 + 9 + (anios_humanos - 2) * 5
        anios_gato = 15 + 9 + (anios_humanos - 2) * 4

print(f'{anios_humanos} años humanos equivalen a {anios_perro} años de perro y a {anios_gato} años de gato.')
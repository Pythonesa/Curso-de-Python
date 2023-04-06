'''
    Pedir al usuario que ingrese su estado de humor y 
    mostrar un emoji que lo represente y un emoji de alerta si el estado de humor no se encuentra en la lista.
'''

feliz = chr(0x1F600)
triste = chr(0x1F62D)
suenio = chr(0x1F634)
enamorado = chr(0x1F60D)
alerta = chr(0x26A0)

estado = input("Ingrese su estado de humor (feliz, triste, con sueño o enamorado): ")
match estado:
    case 'feliz':
        print(feliz)
    case 'triste':
        print(triste)
    case 'con sueño':
        print(suenio)
    case 'enamorado':
        print(enamorado)
    case _:
        print(alerta)
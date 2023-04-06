'''
    Escribir un programa que adivine un personaje en base a tres preguntas 
    (debe incluír un total de 8 personajes, uno por cada combinación).
'''

print("Piense en un personaje de los siguientes: IronMan, Capitana Marvel, Ronan el acusador, Vision, Spiderman, Hulk, Rayo negro o Thanos. Responda si o no a las siguientes preguntas:")
vuela = input("Puede volar? ")
humano = input("Es humano? ")
mascara = input("Tiene máscara? ")

if vuela == 'si':
    if humano =='si':
        if mascara == 'si':
            print("Su personaje es Ironman.")
        else:
            print("Su personaje es la Capitana Marvel.")
    else:
        if mascara == 'si':
            print("Su personaje es Ronan, el acusador.")
        else:
            print("Su personaje es Vision.")
else:
    if humano == 'si':
        if mascara == 'si':
            print("Su personaje es Spiderman.")
        else:
            print("Su personaje es Hulk.")
    else:
        if mascara == 'si':
            print("Su personaje es Rayo Negro.")
        else:
            print("Su personaje es Thanos.")

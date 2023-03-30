'''
    Existe una formula para calcular el rango de edades recomendado para una cita (para mayores de 14 años). 
    El mínimo se calcula como la mitad de la edad más 7 
    y el máximo como el doble de la edad menos 7. 
    Pedir la edad al usuario 
    y mostrarle el rango de edades para sus citas (redondeando al entero más cercano).
'''

print("No salgas con alguien cuya edad no te conviene! Fijate el rango recomendado primero!")

edad = int(input("Ingresa tu edad: "))

min = round(edad / 2 + 7)
max = round(edad * 2 - 7)

print(f'Deberías salir con personas de entre {min} y {max} años.')
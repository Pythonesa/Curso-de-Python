#Escribir un programa que pida al usuario su nombre y apellido en formato título y repita la petición hasta que el formato sea correcto.

nombre = 'no'

while not nombre.istitle():
    nombre = input("Ingrese su nombre y apellido en el siguiente formato: Nombre Apellido. ")
else:
    print("Nombre ingresado en el formato correcto.")
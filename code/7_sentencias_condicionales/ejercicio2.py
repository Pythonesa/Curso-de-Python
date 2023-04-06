'''
    Pedir al usuario que ingrese un año y decirle si es o no un año bisiesto. 
    (Un año es bisiesto si es divisible entre 4 y no es divisible entre 100, o si es divisible entre 400.)
'''

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
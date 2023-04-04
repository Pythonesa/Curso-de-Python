#Pida al usuario dos números enteros y muestre el resultado de su suma, resta y multiplicación.

numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese un otro número entero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print(f'Operando los números {numero1} y {numero2}, el resultado de la suma es {suma}, de la resta es {resta} y de la multiplicación es {multiplicacion}.')
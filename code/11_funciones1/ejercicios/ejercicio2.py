"""
Crear una calculadora, 
pidiendo al usuario que ingrese dos números y la operación que desea realizar, 
mostrar el resultado y preguntar si desea realizar otra operación 
(cada operación deberá ser calculada en una función lambda)
"""

suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a,b: a / b

seguir = True

while seguir:
    a = float(input("Ingrese el primero número: "))
    b = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese el símbolo de la operación que desea ralizar:" +
                      "(suma: +, resta: -,multiplicación: *, división: /): ")
    match operacion:
        case '+':
            print(f'El resultado de la suma es: {suma(a,b)}')
        case '-':
            print(f'El resultado de la resta es: {resta(a,b)}')
        case '*':
            print(f'El resultado de la multiplicación es: {multiplicacion(a,b)}')
        case '/':
            print(f'El resultado de la división es: {division(a,b)}')
        case _:
            print("Operación ingresada no válida.")
    
    opcion = input("Desea seguir [s/n]: ")
    if opcion == 'n' or 'N':
        seguir = False

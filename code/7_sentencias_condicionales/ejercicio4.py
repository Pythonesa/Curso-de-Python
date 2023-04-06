'''
    Pedir al usuario dos números y una operación matemática (suma, resta, multiplicación o división) y 
    mostrar el resultado de la operación elegida (si la operación elegida no es una de las opciones, mostrar un mensaje de error).
'''

num1 = float(input("Ingrese el primero número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese el signo de la operación deseada(+, -, * o /): ")

match operacion:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        resultado = "ERROR: operación ingresada no válida."

print(f'El resultado de {num1} {operacion} {num2} es {resultado}')
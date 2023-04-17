'''
def obtener_suma_resta(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    return suma, resta


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

suma, resta = obtener_suma_resta(num1, numero2=num2)

print(f'El resultado de la suma es: {suma}, y de la resta es: {resta}')
'''
'''
lista = ['Lam277', 'Pinnackles']
contador = 2

nombre = 'DHardySD'

def agregar_usuario(nick: str, contador: int, lista: list =[]) -> tuple:
    """Añade el nombre de un usuario a la lista de usuarios activos.
       Retorna contador de tipo int y la lista de usuarios modificada.
    """
    copia_lista = lista.copy()
    copia_lista.append(nick)
    contador += 1
    return contador, copia_lista


contador, lista = agregar_usuario(nombre, contador)
print(lista, contador)
'''

suma = lambda num1, num2: num1 + num2

print(suma(5, 2))


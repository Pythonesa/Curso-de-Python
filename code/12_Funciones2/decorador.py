'''
Funciones que modifican el comportamiento de otras funciones.
Ayudan a acortar nuestro código (hacen que sea más pitónico).
Para utilizar un decorador basta con utilizar en la línea previa
a la función objetivo @nombre_decorador
'''

# Un decorador que encapsula la función que se pasa como entrada.


def decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar a una función.")
        c = funcion(a, b)
        print("La función ya finalizó.")
        return c
    return nueva_funcion


@decorador
def suma(a, b):
    print("Dentro de la función suma.")
    return a + b


@decorador
def resta(a, b):
    print("Dentro de la función resta.")
    return a - b


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = suma(a, b)
resta = resta(a, b)

print(f'El resultado de la suma es {suma} y de la resta es {resta}.')

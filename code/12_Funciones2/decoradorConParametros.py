'''
Podemos darle parámetros a un decorador para modificar su comportamiento.
Lo hacemos envolviendo una vez más la función.
'''


def decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print("La función ya finalizó.")
            return c
        return nueva_funcion
    return decorador_real


@decorador("Llamando a la función suma.")
def suma(a, b):
    print("Dentro de la función suma.")
    return a + b


@decorador("Llamando a la función resta.")
def resta(a, b):
    print("Dentro de la función resta.")
    return a - b


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = suma(a, b)
resta = resta(a, b)

print(f'El resultado de la suma es {suma} y de la resta es {resta}.')

a = 5; b = 0
d = "hola"
try:
    # if b == 0:
    #     raise ZeroDivisionError
    # else:
    #     c = a / 2
    #     f = a + d
    f = a + b
    try:
        print("Try anidado")
    except Exception as e:
        raise e
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except TypeError:
    print("No se puede sumar un string con un entero.")
except Exception as e:
    print(type(e))
    print("Algo que no es dividir entre cero pasó y no se pudo realizar la división.")
else:
    print("No se ha producido ninguna excepción.")
finally:
    print("Fin del programa. Esto se ejecuta siempre.")
    
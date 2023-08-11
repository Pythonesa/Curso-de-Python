#assert False, "Hicimos fallar esta porquería."

def sumar(numero1, numero2):
    return numero1 + numero2

print(sumar(2, 3))
print(sumar(2, 3) == 5)
assert sumar(2, 3) == 5, "La suma de 2 + 3 no es 5"

class A:
    pass

class B:
    pass

a = B()

assert isinstance(a, A), "a no es una instancia de A"
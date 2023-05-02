'''
Son funciones que en lugar de devolver un valor con return usan yield.
La principal diferencia es que un generador tras ejecutar la línea del yield
devuelve el control de flujo a donde fue llamada pero queda en pausa
y el estado de sus variables es guardado lo que permite reanudar su ejecución.
'''

def generador():
    yield 5

#Un generador devuelve un objeto generador que se debe almacenar en una variable.
print(generador())

#Para obtener el valor que devuelve un generador usamos next()
#a = generador()
#print(next(a))
#print(next(a))

#Un generador puede tener múltiples yields accesibles por next()
# def generadorTriple():
#     contador = 1
#     yield contador

#     contador += 1
#     yield contador

#     contador += 1
#     yield contador

# gt = generadorTriple()
# print(next(gt))
# print(next(gt))
# print(next(gt))


'''
Podemos crear los generadores de una forma más sencilla de la forma
generador = (lo_que_devuelve),
siempre que lo que devuelve sea generado por un for
'''

lista = [1, 2, 3, 5, 6]

generadorCuadrado = (num**2 for num in lista)

print(next(generadorCuadrado))
for num in generadorCuadrado:
    print(num)

# lista.append(7)
# print(next(generadorCuadrado))

'''
Si hacemos el ejemplo anterior con listas el uso de memoria va a ser mayor.
Con los generadores los valores son generados en cada llamada,
en lugar de estar todos almacenados en la memoria.
'''
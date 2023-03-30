'''
    Ejercicio 1: Resolver una ecuación de segundo grado (ax² + bx + c = 0) 
    pidiendo al usuario que ingrese los valores para a, b y c; mostrar los 2 resultados posibles.
'''
#a=4,b=-6,c=2 -> x1=1.0 y x2=0.5
#a=1,b=2,c=-3 -> x1=1.0 y x2=-3.0
#a=-1,b=-2,c=8 -> x1=-4.0 y x2=2.0

print('Bienvenid@, vamos a resolver una ecuación de segundo grado representada: ax² + bx + c = 0')

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(f'Las dos posibles soluciones son: x1 = {x1} y x2: {x2}')

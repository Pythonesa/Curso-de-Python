# Caclular un ángulo de un triángulo a partir de los otros dos ingresados por el usuario.

print('Vamos a calcular cuantos grados tiene el tercer ángulo de un triángulo!')

primer_angulo = float(input("Ingresa los grados del primer ángulo: "))
segundo_angulo = float(input("Ingresa los grados del tercer ángulo: "))

tercer_angulo = 180 - primer_angulo - segundo_angulo

print(f'El tercer ángulo es de {tercer_angulo} grados.')

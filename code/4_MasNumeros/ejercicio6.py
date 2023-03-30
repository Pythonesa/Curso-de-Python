# Pedir una velocidad al usuario en km/h y mostrarla convertida a cm/s.

print("Convierte una velocidad en km/h a cm/s.")
km_x_h = float(input("Ingresa la velocidad en kilómetros/hora: "))
cm_x_s = km_x_h * 27.77777778 #en realidad los 7 despues de la coma son infinitos, pero valia aproximar xD

print(f'Velocidad en centímetros/segundos: {cm_x_s}')
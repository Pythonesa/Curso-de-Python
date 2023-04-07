contador = 0
while contador < 3:
    contador += 1
    if contador == 1:
        continue
    print(f'Contador vale {contador}')
else:
    print("El bucle terminó.")
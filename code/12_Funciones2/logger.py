def log(fichero):
    def decorador_log(funcion):
        def decorador_funcion(*args, **kwargs):
            with open(fichero, 'a') as fichero_abierto:
                salida = funcion(*args, **kwargs)
                fichero_abierto.write(f'{salida}\n')
        return decorador_funcion
    return decorador_log


@log("sumas.log")
def suma(a, b, c):
    return a + b+ c


@log("restas.log")
def resta(a, b):
    return a - b


suma(2, 4, 3)
resta(6, 2)
suma(17, 3, 101)
suma(2, 3.5, 11.05)
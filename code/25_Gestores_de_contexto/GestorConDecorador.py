from contextlib import contextmanager
@contextmanager
def gestor_de_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'w')
        yield archivo
    finally:
        archivo.close( )

with gestor_de_archivo("archivo.txt") as archivo:
    archivo.write("Escribir algo")
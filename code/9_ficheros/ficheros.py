#Los ficheros son un medio de almacenamiento persistente.

'''
    La función open() nos permite trabajar con un fichero de tres formas: leer, escribir y añadir.
    Puede recibir 3 parámetros: ruta, modo('r' por defecto) y codificación(por defecto UTF-8).
    Los modos que podemos usar son: 
        'r' <- lectura (si el fichero no existe lanza un error)
        'w' <- escritura (este modo elimina el contenido anterior del archivo)
        'a' <- añadir (agrega texto al final del fichero)
        'x' <- para crear un archivo, lanza un error si el fichero existe
        'b' <- abre un archivo en modo binario

    Al usar la función write() en los modos 'w' y 'a' si queremos que haya un salto de línea debemos especificarlo agregandolo -> '\n'

    Para cerrar un fichero tenemos la opcion de usar la función close(), aunque es mejor usar contexto.

    Al utilizar contextos al abrir ficheros nos aseguramos de que el contexto se asegure de cerrarlo adecuadamente y así liberar sus recursos.
    Es una buena practica ya que los cierra adecuadamente, incluso si ocurre un error.
    Para usar contextos tenemos la palabra reservada -> with
'''
lineas = []
with open('saludo', 'r') as fichero:
    lineas = fichero.readlines()

for linea in lineas:
    print(linea)
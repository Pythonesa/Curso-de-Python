'''
    Crear un programa que muestre en consola el texto de un archivo 
    y pregunte al usuario si desea añadir más entradas, 
    en caso de desearlo debe poder ingresar las entradas que desee 
    y escribirlas en el fichero.
'''

path = 'ficheros/test1'
#path = input("Ingrese el path y nombre del archivo: ")

with open(path) as fichero:
    for linea in fichero:
        print(linea, end="") #end="" -> el print() no hace un salto de línea

agregar = input("Desea agregar más entradas? [s/n]: ").lower()

lineas_agregar = []

if agregar == 's':
    while agregar != 'n':
        lineas_agregar.append(input("Ingrese una nueva línea a agregar: ") + '\n')
        agregar = input("Desea agregar más entradas? [s/n]: ").lower()
    else:
        with open(path, 'a') as fichero:
            fichero.writelines(lineas_agregar)

'''
    Crear un programa que escriba lo que entre el usuario en la consola 
    (el usuario puede escribir una frase 
    y luego el programa deberá preguntarle si desea seguir escribiendo o no) 
    en un archivo llamado como desee el usuario, si el fichero existe sobrescribirlo.
'''

#Ingreso de datos por parte del usuario:
nombre_fichero = input("Ingrese el nombre deseado para el archivo: ")

salir = 'n'
lineas = []

while salir != 's':
    lineas.append(input("Ingrese una línea para su archivo: ") + '\n')
    salir = input("Desea salir [s/n]: ").lower()
else:
    #Trabajo con el fichero:
    with open(f'ficheros/{nombre_fichero}', 'w') as fichero:
        fichero.writelines(lineas)
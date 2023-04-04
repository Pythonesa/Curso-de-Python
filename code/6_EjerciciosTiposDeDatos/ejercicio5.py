'''
    Pida al usuario que ingrese la ruta de un recurso samba (formato: //1.1.1.1/dir/hola o //samba-server/dir/hola) 
    y muestre por separado el host(1.1.1.1 o samba-server) de el path (/dir/hola).
'''

ruta = input("Ingrese la ruta de un recurso samba: ")

#string.find(value, start, end)
#Buscamos el primer '/' saltandonos los primeros dos caracteres:
separador = ruta.find('/' , 2)

host = ruta[2:separador]
path = ruta[separador:]

print(f'El host es {host} y el path es {path}.')
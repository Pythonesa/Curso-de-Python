#Multiplicar x 3 los elementos de una lista.

#Sin map:
# lista = [1, 2, 3, 4, 5]
# lista_por_tres = []

# for item in lista:
#     lista_por_tres.append(item * 3)

# print(lista_por_tres)


#Con map:
# lista_map = [1, 2, 3, 4, 5]


# def por_tres(numero):
#     return numero * 3


# map_por_tres = map(por_tres, lista_map)

# print(map_por_tres)
# print(list(map_por_tres))

#Con map, lambda y next:
otra_lista = [1, 2, 3, 4, 5]
map_x_tres = map(lambda num: num*3, otra_lista)

print(next(map_x_tres))
print(next(map_x_tres))
print(next(map_x_tres))
print(next(map_x_tres))
print(next(map_x_tres))
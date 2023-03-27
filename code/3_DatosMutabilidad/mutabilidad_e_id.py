entero = 5
print(f'La variable entero contiene un valor de {entero}, de tipo {type(entero)} y apunta a {id(entero)}')
segundo_entero = entero
print(f'La variable segundo_entero contiene un valor de {segundo_entero}, de tipo {type(segundo_entero)} y apunta a {id(segundo_entero)}')
entero = 7
print(f'La variable entero contiene un valor de {entero}, de tipo {type(entero)} y apunta a {id(entero)}')
print(f'La variable segundo_entero contiene un valor de {segundo_entero}, de tipo {type(segundo_entero)} y apunta a {id(segundo_entero)}')
lista = [1,2,3]
print(f'La variable lista contiene un valor de {lista}, de tipo {type(lista)} y apunta a {id(lista)}')
lista[0] = 5
print(f'La variable lista contiene un valor de {lista}, de tipo {type(lista)} y apunta a {id(lista)}')

def cambiar_numero(numero,lista_numeros):
    numero = 12
    lista_numeros[1] = 12

cambiar_numero(entero,lista)

print(f'La variable entero contiene un valor de {entero}, de tipo {type(entero)} y apunta a {id(entero)}')
print(f'La variable lista contiene un valor de {lista}, de tipo {type(lista)} y apunta a {id(lista)}')
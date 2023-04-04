'''
    Pida al usuario que ingrese un texto, 
    luego pida que ingrese una palabra del texto que desee cambiar 
    y la palabra por la cual desea cambiarla; 
    muestre en pantalla el texto modificado.
'''

texto = input("Ingrese un texto: ")
palabra_cambiar = input("Ingrese la palabra que desea cambiar: ")
palabra_final = input("Ingrese la palabra por la cual quiere cambiarla: ")

texto_final = texto.replace(palabra_cambiar, palabra_final)

print(texto_final)
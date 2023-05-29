'''
Al utilizar el decorador @property sobre un método hará que funcione como un atributo.
Vamos a entender mejor todo esto cuando veamos Encapsulamiento.
Pero, en determinadas ocasiones es importante ocultar el estado interno de los objetos al exterior.
Utilizamos __ antes del nombre del atributo para decirle a Python que queremos que la oculte
y que no pueda ser accedida como el resto de los atributos.
El acceso a través de un método nos garantiza un acceso controlado a nuestro atributo.
'''

class Caja:
    def __init__(self, color):
        self.__color = color

    #@property nos permite obtener el valor del atrabuto (getter)
    @property
    def color(self):
        return self.__color
    
    #@atributo.setter nos permite darle un valor al atributo (setter)
    #Muy útil cuando tenemos que controlar el ingreso del valor, aparte de encapsulamiento.
    @color.setter
    def color(self, color):
        self.__color = color




caja1 = Caja("rojo");
#Si intentamos llamar a color como un método dará error:
#caja1.color()

#Pero si podemos acceder a color como un atributo:
print(caja1.color)

caja1.color = "azul"
print(caja1.color)


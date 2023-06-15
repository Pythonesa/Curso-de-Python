class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    #Métodos genéricos que cada hija deberá implementar:
    def hablar(self):
        pass

    def moverse(self):
        pass

    #Método genérico general:
    def definirse(self):
        print(f"Animal de tipo {type(self).__name__}.")


class Gato(Animal):
    def __init__(self, especie, edad, duenio):
        super().__init__(especie, edad)
        self.duenio = duenio
    #Sobreescribe métodos de la clase padre:
    def hablar(self):
        print("¡Miau!")

    def moverse(self):
        print("Caminando con 4 patas.")
    
    #Implementación propia:
    def araniar(self):
        print("Araña.")


# print(Gato.__bases__)
# print(Animal.__subclasses__())

# gato1 = Gato("Mamífero", "3 años")
gato1 = Gato("Mamífero", "3 años", "Pepe")

print(gato1.definirse())

gato1.hablar()
gato1.moverse()
gato1.araniar()

print(gato1.especie)
print(gato1.duenio)

# print(Gato.__mro__)
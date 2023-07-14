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
        

class Perro(Animal):
    def __init__(self, especie, edad, duenio):
        super().__init__(especie, edad)
        self.duenio = duenio
    #Sobreescribe métodos de la clase padre:
    def hablar(self):
        print("¡Guau!")

    def moverse(self):
        print("Caminando con 4 patas.")
        
        
def hacer_hablar(animal):
    animal.hablar()
    
perro = Perro("dalmata", 5, "Pepe")
gato = Gato("siames", 2, "Pepito")

hacer_hablar(perro)
hacer_hablar(gato)

print(3 * 3)
print("hola" * 3)
class InformalPetInterface():
    def talk():
        pass
    def walk():
        pass

class Dog(InformalPetInterface):
    def talk():
        return "Guau guau!"
    def walk():
        return "Camina en cuatro patas"
    
class Cat(InformalPetInterface):
    def talk():
        return "Miau miau!"
    
print(Dog.talk())
print(Dog.walk())
print(Cat.talk())
print(Cat.walk())

print(issubclass(Dog, InformalPetInterface))
print(issubclass(Cat, InformalPetInterface))
print(Dog.__mro__)
print(Cat.__mro__)

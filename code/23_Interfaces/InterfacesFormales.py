from abc import ABCMeta, abstractmethod

class PetInterface(metaclass=ABCMeta):
    @abstractmethod
    def talk(self):
        pass
    @abstractmethod
    def walk(self):
        pass
    
class Dog(PetInterface):
    def talk(self):
        return "Guau guau!"
    def walk(self):
        return "Camina en 4 patas"
    
class Cat(PetInterface):
    def talk(self):
        return "Miau miau!"
    
d = Dog()
print(d.talk())
print(d.walk())

#c = Cat()

print(issubclass(Dog, PetInterface))
print(issubclass(Cat, PetInterface))
print(Dog.__mro__)
print(Cat.__mro__)
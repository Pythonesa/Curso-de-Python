class PetMeta(type):
    def __intancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'talk') and callable(subclass.talk) and
                hasattr(subclass, 'walk') and callable(subclass.walk))
        
class InformalPetInterface(metaclass=PetMeta):
        pass
        
class Dog():
    def talk():
        return "Guau guau!"
    def walk():
        return "Camina en cuatro patas"
    
class Cat():
    def talk():
        return "Miau miau!"
    
print(Dog.talk())
print(Dog.walk())
print(Cat.talk())
#print(Cat.walk())

print(issubclass(Dog, InformalPetInterface))
print(issubclass(Cat, InformalPetInterface))
print(Dog.__mro__)
print(Cat.__mro__)
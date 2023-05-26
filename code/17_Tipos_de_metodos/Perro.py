class Perro:
    especie = "Canis lupus familiaris"

    def __init__(self, nombre, raza, sexo, edad):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.edad = edad

    #Método de instancia
    def adoptar(self, nombre):
        self.nombre = nombre

    #Método de clase
    @classmethod
    def cambiar_especie(cls, especie):
        cls.especie = especie

    #Método estático
    @staticmethod
    def ladrar():
        print("Guau, guau!")

    


print(Perro.especie)

kaly = Perro("Maira", "Puro Perro", "Hembra", 2)
print(f'{kaly.nombre} tiene {kaly.edad} años, es de raza {kaly.raza} y es {kaly.sexo}; su especie es {kaly.especie}.')
kaly.adoptar("Kaly")
print(f'Ahora fue adoptada y se llama {kaly.nombre}')
kaly.ladrar()
Perro.ladrar()
print(kaly.especie)
print(Perro.especie)
Perro.cambiar_especie("Canino")
print(Perro.especie)
print(kaly.especie)
class Persona:
    nombre = "Pepe"
    __edad = 18
    _cantidad_mascotas = 2
    
    def setEdad(edad):
        if edad > 0 and edad < 150:
            Persona.__edad = edad
    def getEdad():
        return Persona.__edad
    
    
    
print(Persona.nombre)
print(Persona._Persona__edad)
print(Persona._cantidad_mascotas)
Persona.setEdad(30)
print(Persona.getEdad())
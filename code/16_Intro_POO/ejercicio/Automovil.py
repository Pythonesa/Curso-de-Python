class Automovil:
    ruedas = 4

    def __init__(self, marca, modelo, motor, potencia, velocidad_maxima, 
                 color, puertas):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.potencia = potencia
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.puertas = puertas
        self.velocidad_actual = 0

    def get_info(self):
        info = f'Marca: {self.marca}, modelo: {self.modelo}, \
motor: {self.motor}, potencia: {self.potencia}, \
velocidad máxima: {self.velocidad_maxima}km/h, \
color: {self.color}, cantidad de ruedas: {self.ruedas}, \
cantidad de puertas: {self.puertas}.'
        return info
    
    def acelerar(self, velocidad):
        if self.velocidad_actual + velocidad <= self.velocidad_maxima:
            self.velocidad_actual += velocidad
        elif self.velocidad_actual + velocidad >= self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        
    def reducir_velocidad(self, velocidad):
        if self.velocidad_actual - velocidad >= 0:
            self.velocidad_actual -= velocidad
        else:
            self.velocidad_actual = 0
    
    def pintar(self, color):
        self.color = color

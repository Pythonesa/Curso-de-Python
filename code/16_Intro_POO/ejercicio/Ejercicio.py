from Automovil import Automovil

ecto1 = Automovil("Cadillac", "Miller Meteor", 
                  "V8 de 6,4 litros de cilindrada", "330 CV", 180, 
                  "blanco", 4)
kitt = Automovil("Pontiac", "Firebird Trans Am", 
                 "V8 de 5,0 litros de cilindrada", "180 CV", 180, "negro", 2)
batimovil = Automovil("Chevrolet", "Impala", "Rolls Royce", "350 CV", 530, 
                      "negro", 2)
delorean = Automovil("DMC", "DeLorean", "V6 de 2,8 litros de cilindrada",
                     "132 CV", 200, "gris", 2)

print(ecto1.get_info())
print(kitt.get_info())
print(batimovil.get_info())
print(delorean.get_info())

delorean.pintar("amarillo")
print(f"El DeLorean ahora es de color {delorean.color}.")

delorean.acelerar(60)
print(f"Vas a {delorean.velocidad_actual}km/h.")
delorean.acelerar(110)
print(f"Vas a {delorean.velocidad_actual}km/h.")
delorean.acelerar(60)
print(f"Vas a {delorean.velocidad_actual}km/h.")

print("Bienvenid@ al pasado!!!")

delorean.reducir_velocidad(80)
print(f"Vas a {delorean.velocidad_actual}km/h.")
delorean.reducir_velocidad(100)
print(f"Vas a {delorean.velocidad_actual}km/h.")
delorean.reducir_velocidad(60)
print(f"Vas a {delorean.velocidad_actual}km/h.")
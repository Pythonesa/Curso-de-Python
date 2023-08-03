# class ExcepcionPersonalizada(Exception):
#     def __init__(self, mensaje, informacion):
#         self.mensaje = mensaje
#         self.informacion = informacion

# a = "hola"
# try:
#     if a == "hola":
#         raise ExcepcionPersonalizada("Excepción Personalizada", "Fue lanzada por hola")
# except ExcepcionPersonalizada as e:
#     print(f'Mensaje: {e.mensaje}')
#     print(f'Información: {e.informacion}')

class OtraExcepcion(Exception):
    pass
try:
    raise OtraExcepcion({"mensaje":"El mensaje del error",    
        "informacion":"La información del error"})
except OtraExcepcion as e:
    detalles = e.args[0]
    print(detalles["mensaje"])
    print(detalles["informacion"])
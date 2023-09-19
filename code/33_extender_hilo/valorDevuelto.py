from threading import Thread

class hiloExtendido(Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.numero = len(nombre)
    
    def run(self):
        print(self.nombre)
        
    
        
        
def main():
    nombres = ["Kaly", "Pepe", "Juan", "Pedro", "María", "Eustaquio", "José", "Pablo", "Laura", "Pía"]
    hilos = [hiloExtendido(nombre) for nombre in nombres]
    for hilo in hilos:
        hilo.start()
        cantidad_letras = hilo.numero
        hilo.join()
        print("Cantidad de letras: ", cantidad_letras)
        

if __name__ == "__main__":
    main()
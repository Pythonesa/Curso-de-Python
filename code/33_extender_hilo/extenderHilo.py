from threading import Thread

class hiloExtendido(Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def run(self):
        print(self.nombre)
        
        
def main():
    nombres = ["Kaly", "Pepe", "Juan", "Pedro", "María", "Eustaquio", "José", "Pablo", "Laura", "Pía"]
    hilos = [hiloExtendido(nombre) for nombre in nombres]
    for hilo in hilos:
        hilo.start()
        hilo.join()

if __name__ == "__main__":
    main()
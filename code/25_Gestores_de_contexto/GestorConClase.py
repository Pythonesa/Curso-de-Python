class Indice:
    def __init__(self):
        self.level = -1
        self.numeracion = [0]

    def __enter__(self):
        self.level += 1
        self.numeracion.append(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.numeracion[self.level] = 0
        self.numeracion.pop()
        self.level -= 1

    def print(self, text):
        self.numeracion[self.level] += 1
        numer = [str(i) for i in self.numeracion[:self.level+1]]
        print(f"{'  '*self.level}{'.'.join(numer)} {text}")
        

with Indice() as indice:
    indice.print('Apartado')
    with indice:
        indice.print('Apartado')
        indice.print('Apartado')
        indice.print('Apartado')
        indice.print('Apartado')
        with indice:
            indice.print('Apartado')
            indice.print('Apartado')
            with indice:
                indice.print('Apartado')
                indice.print('Apartado')
    indice.print('Apartado')
    indice.print('Apartado')
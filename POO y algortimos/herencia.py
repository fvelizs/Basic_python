class Figura:
    def __init__(self, base, altura):
        self.base =base
        self.altura = altura

    
    def area (self):
        return self.base*self.altura


class Cuadrado(Figura):

    def __init__(self, base):
        super().__init__(base, base)

class Rectangulo (Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

if __name__=='__main__':
    rectagunlo = Rectangulo (base =4, altura=3)
    print(rectagunlo.area())
    cuadrado = Cuadrado(base=4)
    print(cuadrado.area())
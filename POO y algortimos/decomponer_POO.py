class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.estado = "en reposo"
        self.motor = Motor(cilindros=4)

    def acelerar (self, tipo="despacio"):
        if tipo=="rapido":
            self.motor.inyecta_gasolina(30)
        else:
            self.motor.inyecta_gasolina(10)
        self._estado = "en movimiento"


class Motor:

    def __init__ (self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self.temperatura = 0

    def inyecta_gasolina (self, cantidad):
        pass

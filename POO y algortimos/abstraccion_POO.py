class Lavadora:
    
    def __init__(self):
        pass

    def lavar (self, temperatura):
        self._llenar_tanque(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._secar()
        
    
    def _llenar_tanque (self, temperatura):
        print(f'llenaando el tanque con agua a {str(temperatura)}°')

    def _añadir_jabon (self):
        print("añadiendo jabon")

    def _lavar(self):
        print("lavando la ropa")

    def _secar (self):
        print("secando la ropa")

if __name__ == '__main__':
    lavadora = Lavadora()
    temperatura = int(input("ingrese tempratura: "))
    lavadora.lavar(temperatura)
    
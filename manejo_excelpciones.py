
def divide (lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return "no se puede dividir por 0"


def run():
    lista = list(range(10))
    divisor = 0
    print(divide(lista, divisor))

if __name__=='__main__':
    run()
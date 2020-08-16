import random

def run():
    numero = random.randint(1,10000)
    inicio=0
    fin=10000

    respuesta = input(f'el numero que esta pensando es mayor, menor o igua a {numero}? ')

    while respuesta != "igual":
        if respuesta == "mayor":
            inicio = numero + 1
            numero = (inicio + fin)//2
        elif respuesta == "menor":
            fin = numero - 1
            numero = (inicio + fin) //2

        respuesta = input(f'el numero que esta pensando es mayor, menor o igua a {numero}? ')
    
    print (f'tu numero es: {numero}')


if __name__=='__main__':
    run()

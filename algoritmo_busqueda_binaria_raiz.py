def run ():
    objetivo = int(input("ingrese numero: "))
    epsilon = 0.000000000001
    alto = objetivo
    bajo = 0.0
    respuesta = (bajo + alto)/2

    if objetivo <= 0:
            print("los numeros negativos no tienen raices reales")
    else:
        while abs(respuesta**2 - objetivo) >= epsilon:
            if respuesta**2 < objetivo:
                bajo = respuesta
            else:
                alto = respuesta

            respuesta = (bajo + alto)/2

    if objetivo<=0:
        print("debe ingresar un numero positivo")
    else:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()
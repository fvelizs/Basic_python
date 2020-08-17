def binaria (objetivo):   
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
        print ("debe ingresar un numero positivo")
    else:
        print (f'la raiz cuadrada de {objetivo} es {respuesta}')

def exhaustiva(numero):

    contador=0
    while contador**2<numero:
        contador+=1

    if contador**2==numero:
        print (f'la raiz cuadrada de {numero} es: {contador}')
    else:
        print(f'{numero} no tiene raiz cuadra exacta') 


def aproximacion (objetivo):
    epsilon = 0.001
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')


def run():

    objetivo = int(input("ingrese numero: "))
    opc= int(input("""ingrese la opcion por la cual quiere calcula la raiz:
    1. Busqueda binaria (recomendada)
    2. aproximacion (la mas lenta)
    3. Enumeracion exhaustiva (solo entrega raices exactas): """))
    if opc==1:
        binaria(objetivo)
    elif opc==2:
        aproximacion(objetivo)
    elif opc==3:
        exhaustiva(objetivo)
    else:
        print(f' la opcion {opc} no es una opcion valida')
        


if __name__=='__main__':
    run()
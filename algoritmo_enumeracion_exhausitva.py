def run():

    numero= int(input("ingrese un numero: "))
    contador=0
    while contador**2<numero:
        contador+=1

    if contador**2==numero:
        print (f'la raiz cuadrada de {numero} es: {contador}')
    else:
        print(f'{numero} no tiene raiz cuadra exacta') 

if __name__=='__main__':
    run()
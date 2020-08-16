def run():
    LIMITE = 10000
    contador=0
    resultado=0

    while (resultado < LIMITE):
        resultado=2**contador
        print ("2 elevado a " + str(contador) + " es igual a: "+ str(resultado))   
        contador = contador+1


if __name__ == '__main__':
    run()
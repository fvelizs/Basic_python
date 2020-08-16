def tabla (menu):
    contador=1
    for i in range(10):
        resultado= contador*menu
        print (str(menu)+"*"+str(contador)+"= "+str(resultado))
        contador+=1


def run():
    #ejemplo ciclo while comentado
#     LIMITE = 10000
#     contador=0
#     resultado=0

#     while (resultado < LIMITE):
#         resultado=2**contador
#         print ("2 elevado a " + str(contador) + " es igual a: "+ str(resultado))   
#         contador = contador+1

    menu= int(input("""Ingrese la la tabla que desea conocer: """))
    tabla(menu)

if __name__ == '__main__':
    run()
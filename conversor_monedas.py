menu = """
Bienvenido a su conversor favorito, 

1- Pesos Chilenos a Dolares
2- Soles peruanos a Dolares
3- Pesos Mexicanos a Dolares

por favor ingrese una opcion: """
opc = int(input(menu))
if opc == 1:
    pesos = int(input("ingrese cantidad de pesos que tiene: "))
    valor_dolar= 750
    resultado= round(pesos/valor_dolar,2)
    print("usted tiene $"+ str(resultado)+" dolares")
elif opc == 2:
    pesos = int(input("ingrese cantidad de pesos que tiene: "))
    valor_dolar= 3.5
    resultado= round(pesos/valor_dolar,2)
    print("usted tiene $"+ str(resultado)+" dolares")
elif opc == 3:
    pesos = int(input("ingrese cantidad de pesos que tiene: "))
    valor_dolar= 25
    resultado= round(pesos/valor_dolar,2)
    print("usted tiene $"+ str(resultado)+" dolares")
else:
    print(str(opc) + " no es una opcion valida, por favor ingrece una opcion valida")


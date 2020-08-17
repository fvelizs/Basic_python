def conversor (valor_dolar):
    pesos = int(input("ingrese cantidad de pesos que tiene: "))
    resultado= round(pesos/valor_dolar,2)
    print("usted tiene $"+ str(resultado)+" dolares")

menu = """
Bienvenido a su conversor favorito, 

1- Pesos Chilenos a Dolares
2- Soles peruanos a Dolares
3- Pesos Mexicanos a Dolares

por favor ingrese una opcion: """
opc = int(input(menu))

if opc == 1:
    conversor(750)
   
elif opc == 2:
    conversor(3.5)
elif opc == 3:
    conversor(25)
else:
    print(str(opc) + " no es una opcion valida, por favor ingrece una opcion valida")


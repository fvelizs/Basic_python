menu = """
Bienvenido a su conversor favorito, 

1- Pesos Chilenos a Dolares
2- Soles peruanos a Dolares
3- Pesos Mexicanos a Dolares

por favor ingrese una opcion: """
opc = int(input(menu))

def conversor ():
    pesos = int(input("ingrese cantidad de pesos que tiene: "))
    resultado= round(pesos/valor_dolar,2)
    print("usted tiene $"+ str(resultado)+" dolares")
    

if opc == 1:
    valor_dolar= 750
    conversor()
   
elif opc == 2:
    valor_dolar= 3.5
    conversor()

elif opc == 3:
    valor_dolar= 25
    conversor()  
else:
    print(str(opc) + " no es una opcion valida, por favor ingrece una opcion valida")


import random


def run():
    
    aleatorio = random.randint(1,100)
    print(str(aleatorio))
    numero= int(input("adivina el numero que estoy pensando del 1 al 100: "))
    
    while numero != aleatorio:
        if numero < aleatorio:
            print("el numero es mayor")
            
        elif numero > aleatorio:
            print ("el numero es menor")
        
        numero= int(input("elige numero "))
        
    print("ganaste!!!")
        


if __name__ == '__main__':
    run()
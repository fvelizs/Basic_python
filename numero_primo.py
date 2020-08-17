def primos (num):
    contador=0
    if num == 1:
        return False
    else:
        for i in range (1, num + 1):
            if i == 1 or i == num:
                continue
            if num%i == 0:
                contador +=1
        if contador==0:
            return True
        else:
            return False



def run():
    num = int(input("ingrese numero: "))
    if primos(num):
        print("es primo")
    else:
        print("no es primo")


if __name__ == "__main__":
    run()
def factorial (n):
    
    if n ==1:
        return 1
    else:
        a=n * factorial (n-1)
        print(str(n)+", "+str(a))
        return a

n=int(input("ingrese un numero: "))
print(factorial(n))
        
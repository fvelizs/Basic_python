palabra = input("ingrese una palabra: ")
palindromo = palabra [::-1]
print(palindromo)
if palabra==palindromo:
    print("es un palindromo")
else:
    print("no es un palindromo")

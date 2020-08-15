def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    print (palabra)
    inverso = palabra[::-1]
    if inverso==palabra:
        return True
    else:
        return False


def run():
    palabra = input("ingrese una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")
  

if __name__ == "__main__":
    run()

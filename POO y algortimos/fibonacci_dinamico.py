import sys
def fibonnaci (num, memo={}):
    if num == 0 or num==1:
        return 1
    try:
        return memo[num]
    except KeyError:
        resultado = fibonnaci(num-1) + fibonnaci (num-2)
        memo[num] = resultado
        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(6000)
    num = int(input("ingrese numero a calcular "))
    resultado = fibonnaci(num)
    print(resultado)
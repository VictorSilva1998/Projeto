while True:
    try:
        n = int (input ("Digite o número de Discos na Torre de Hanoi: "))
        break
    except ValueError:
        print ("\nUtilize apenas números inteiros!\n")

movimentos = 2**n - 1

print (f"\nPara realizar a Torre de Hanói com {n} discos serão necessários {movimentos} movimentos.")
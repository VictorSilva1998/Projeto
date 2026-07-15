def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

while True:
    try:
        if __name__=='__main__':
            n = int (input ("Digite o número de Discos na Torre de Hanoi: "))
            movimentos = 2**n - 1
            print (f"Para realizar a Torre de Hanói com {n} discos serão necessários {movimentos} movimentos.")
            torre_hanoi(n, "A", "C", "B")
            break
    except ValueError:
        print ("\nUtilize apenas números inteiros!\n")
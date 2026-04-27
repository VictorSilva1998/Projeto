programa {
  funcao inicio() 
  {
    real x,y,total
    inteiro opcao

    enquanto (opcao!=0) {
    escreva ("====== Calculadora ======\n")
    escreva ("\nOpções:\n")
    escreva ("1 - Adição\n")
    escreva ("2 - Subtração\n")
    escreva ("3 - Multiplicação\n")
    escreva ("4 - Divisão\n")
    escreva ("0 - Sair\n")
    escreva ("Escolha uma das opções acima: ")
    leia (opcao)
      escolha (opcao) {
        caso 1:
          escreva ("Digite o primeiro número= ")
          leia (x)
          escreva ("Digite o segundo número= ")
          leia (y)
          total=x+y
          escreva ("O resultado da adição foi ",total,"\n\n")
        pare
        caso 2:
          escreva ("Digite o primeiro número= ")
          leia (x)
          escreva ("Digite o segundo número= ")
          leia (y)
          total=x-y
          escreva ("O resultado da subtração foi ",total,"\n\n")
        pare
        caso 3:
          escreva ("Digite o primeiro número= ")
          leia (x)
          escreva ("Digite o segundo número= ")
          leia (y)
          total=x*y
          escreva ("O resultado da multiplicação foi ",total,"\n\n")
        pare
        caso 4:
          escreva ("Digite o primeiro número= ")
          leia (x)
          escreva ("Digite o segundo número= ")
          leia (y)
          total=x/y
          escreva ("O resultado da divisão foi ",total,"\n\n")
        pare
        caso 0:
          escreva ("Saindo.....")
        pare
        caso contrario:
          escreva ("\nOpção Invalida!\n\n")
      }
    }
  }
}

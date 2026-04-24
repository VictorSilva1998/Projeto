programa {
  funcao inicio() 
  {
   real cachorro_quente=11.2,ovo_simples=8.3,bauru_com_ovo=11.5,hamburguer=16.2,refrigerante=6,suco=7.5,agua=4.7,sanduiche,bebida,total
   inteiro codigo_sanduiche,codigo_bebida

   escreva ("Digite o código do sanduíche desejado: ")
   leia (codigo_sanduiche)
   escreva ("Digite o código da bebida desejado: ")
   leia (codigo_bebida)

   escolha (codigo_sanduiche) {
    caso 100:
      sanduiche=cachorro_quente
    pare
    caso 101:
      sanduiche=ovo_simples
    pare
    caso 102:
      sanduiche=bauru_com_ovo
    pare
    caso 103:
      sanduiche=hamburguer
    pare
    caso contrario:
      escreva ("\nOpção Invalida!")
   }
   escolha (codigo_bebida) {
    caso 201:
      bebida=refrigerante
    pare
    caso 202:
      bebida=suco
    pare
    caso 203:
      bebida=agua
    pare
    caso contrario:
      escreva ("\nOpção Invalida!")
   }
   total=sanduiche+bebida
   escreva ("O valor total a pagar é de: ",total)
  }
}

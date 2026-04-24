programa {
  funcao inicio() {
    inteiro x,idade

    para (x=1;x<=200;x=x+1) {
      escreva (x," - Digite a sua idade: ")
      leia (idade)
      se (idade<18) {
        escreva ("Menor de Idade.\n\n")
      }
      senao {
        escreva ("Maior de Idade.\n\n")
      }
    }
  }
}
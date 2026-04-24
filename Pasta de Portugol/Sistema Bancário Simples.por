programa {
  funcao inicio() 
  {
   inteiro agencia,conta,choice=0
   cadeia nome,senha
   real saldo=0,saque,deposito

    escreva ("\n===================================================\n")
    escreva ("         BANCO PORTUGOL - SISTEMA BANCÁRIO         ")
    escreva ("\n===================================================\n")
    escreva ("       Bem-vindo ao terminal de atendimento        ")
    escreva ("\n===================================================\n")
    escreva ("       Segurança ° Rapidez ° Confiança             ")
    escreva ("\n===================================================\n")

      enquanto (choice!=5) {
        escreva ("\n===== MENU DO BANCO =====\n")
        escreva ("1 - Cadastro\n")
        escreva ("2 - Ver Saldo\n")
        escreva ("3 - Saque\n")
        escreva ("4 - Depósito\n")
        escreva ("5 - Sair\n")
        escreva ("Escolha uma opção: ")
        leia (choice)
          escolha (choice) {
            caso 1:
              escreva ("\nPara realizar o cadastro informe as informções abaixo:\n")
              escreva ("\nDigite o seu nome: ")
              leia (nome)
              escreva ("Digite a sua agência bancária: ")
              leia (agencia)
              escreva ("Digite o número da conta: ")
              leia (conta)
              escreva ("Digite a sua senha: ")
              leia (senha)
              escreva ("Digite o valor do saldo inicial da conta: R$ ")
              leia (saldo)
              escreva ("\nInformações salvas.\n")
            pare
            caso 2:
              escreva ("\nNome do Cliente: ",nome)
              escreva ("\nNúmero da agência: ",agencia)
              escreva ("\nSeu saldo na conta é: R$ ",saldo,"\n")
            pare
            caso 3:
              escreva ("\nDigite o valor que desejar sacar: R$ ")
              leia (saque)
                se (saldo<saque) {
                  escreva ("\nSaldo Insuficiente\n")
                }
                senao {
                  saldo=saldo-saque
                  escreva ("\nSaldo pós saque: R$ ",saldo,"\n")
                }
            pare
            caso 4:
              escreva ("\nDigite o valor do depósito: R$ ")
              leia (deposito)
              saldo=saldo+deposito
              escreva("\nSaldo pós depósito: R$ ",saldo,"\n")
            pare
            caso 5:
              escreva ("\nSaindo da conta. Muito Obrigado e Tenha um Bom Dia!")
            pare
            caso contrario:
              escreva ("\nOpção Invalida!\n")
      }
    }
  }
}
programa {
  funcao inicio() 
  {
   inteiro senha=1234,agencia=1234,conta=1234,contausuario,senhausuario,agenciausuario,escolha_cliente=1
   real saldo=10000,pagamento,saque,deposito

    escreva ("\n===================================================\n")
    escreva ("          BANCO PYTHON - SISTEMA BANCÁRIO          ")
    escreva ("\n===================================================\n")
    escreva ("       Bem-vindo ao terminal de atendimento        ")
    escreva ("\n===================================================\n")
    escreva ("       Segurança ° Rapidez ° Confiança             ")
    escreva ("\n===================================================\n")
    escreva ("\nDigite o número da sua agência: ")
    leia (agenciausuario)
    escreva ("Digite o número da sua conta: ")
    leia (contausuario)
    escreva ("Digite o número da sua senha: ")
    leia (senhausuario)

    se (agencia==agenciausuario e senha==senhausuario e conta==contausuario) {
      escreva ("\nAcesso Permitido!\n")
      enquanto (escolha_cliente!=0) {
        escreva ("\n===== MENU DO BANCO =====\n")
        escreva ("1 - Saldo\n")
        escreva ("2 - Extrato\n")
        escreva ("3 - Pagamento\n")
        escreva ("4 - Saque\n")
        escreva ("5 - Depósito\n")
        escreva ("0 - Sair\n")
        escreva ("Escolha uma opção: ")
        leia (escolha_cliente)
          escolha (escolha_cliente) {
            caso 1:
              escreva ("\nSeu saldo na conta é: R$ ",saldo,"\n")
            pare
            caso 2:
              escreva ("\nExibindo seu extrato da conta abaixo:\n")
              escreva ("\nPagamento de salário recebido: R$ 10.000,00\n")
            pare
            caso 3:
              escreva ("\nDigite o valor do pagamento: R$ ")
              leia (pagamento)
              saldo=saldo-pagamento
              escreva ("\nSaldo pós pagamento: R$ ",saldo,"\n")
            pare
            caso 4:
              escreva ("\nDigite o valor que desejar sacar: R$ ")
              leia (saque)
              saldo=saldo-saque
              escreva ("\nSaldo pós saque: ",saldo,"\n")
            pare
            caso 5:
              escreva ("\nDigite o valor do depósito: R$ ")
              leia (deposito)
              saldo=saldo+deposito
              escreva("\nSaldo pós depósito: ",saldo,"\n")
            pare
            caso 0:
              escreva ("\nSaindo da conta. Muito Obrigado e Tenha um Bom Dia!")
            pare
            caso contrario:
              escreva ("\nOpção Invalida!\n")
        }
      }
    }
    senao {
      escreva ("\nAcesso Negado")
    }
  }
}

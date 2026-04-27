programa {
  funcao inicio() 
  {
    inteiro senha=1234,agencia=1234,conta=1234,contausuario,senhausuario,agenciausuario,escolha_cliente
    real saldo=10000,resultado,pagamento,saque,deposito
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
      escreva ("\n\n===== MENU DO BANCO =====\n")
      escreva ("1 - Saldo\n")
      escreva ("2 - Extrato\n")
      escreva ("3 - Pagamento\n")
      escreva ("4 - Saque\n")
      escreva ("5 - Depósito\n")
      escreva ("0 - Sair\n")
      escreva ("Escolha uma opção: ")
      leia (escolha_cliente)
      se (escolha_cliente==1) {
        escreva ("\nSeu saldo na conta é: R$ ",saldo)
      }
      senao se (escolha_cliente==2) {
        escreva ("\nExibindo seu extrato da conta abaixo:\n")
        escreva ("\nPagamento de salário recebido: R$ 10.000,00")
      }
      senao se (escolha_cliente==3) {
        escreva ("\nDigite o valor do pagamento: ")
        leia (pagamento)
        resultado=saldo-pagamento
        escreva ("\nSaldo pós pagamento: R$ ",resultado)
      }
      senao se (escolha_cliente==4) {
        escreva ("\nDigite o valor que desejar sacar: ")
        leia (saque)
        resultado=saldo-saque
        escreva ("\nSaldo pós saque: ",resultado)
      }
      senao se (escolha_cliente==5) {
        escreva ("\nDigite o valor do depósito: ")
        leia (deposito)
        resultado=saldo+deposito
        escreva("\nSaldo pós depósito: ",resultado)
      }
      senao se (escolha_cliente==0) {
        escreva ("\nSaindo da conta. Muito Obrigado e Tenha um Bom Dia!")
      }
      senao {
        escreva ("\nOpção Invalida!")
      }
    }
    senao {
      escreva ("\nAcesso Negado")
    }
  }
}
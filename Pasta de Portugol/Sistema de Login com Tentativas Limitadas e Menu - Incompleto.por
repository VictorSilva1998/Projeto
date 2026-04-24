programa {
  funcao inicio() {
    inteiro choice,senha,password=1234
    cadeia usuario

    escreva ("Digite o seu usúario: ")
    leia (usuario)
    escreva ("Digite a sua senha: ")
    leia (senha)
    se (usuario=="admin" e senha==password) {
      escreva ("\nAcesso Permitido!\n")
      enquanto (choice!=4) {
        escreva ("\n1 - Alterar Senha")
        escreva ("\n2 - Mostrar dados de usúarios")
        escreva ("\n3 - Fazer logout")
        escreva ("\n4 - Sair do Sistema\n\n")
        escreva ("Escolha uma opção: ")
        leia (choice)

        escolha (choice) {
          caso 1: 
            escreva ("\nDigite a senha atual: ")
            leia (senha)
            se (senha!=password) {
              escreva ("\nSenha Invalida\n")
            }
            senao se (senha==password) {
              escreva ("Digite a nova senha: ")
              leia (senha)
                se (senha=="" ou senha==password) {
                  escreva ("\nSenha Invalida\n")
                }
                senao {
                  password=senha
                  escreva ("\nSenha Alterada\n")
                }
            }
          pare
          caso 2:
            escreva ("\nNome do Usúario: ",usuario)
            escreva ("\nSenha do Usúario: ",senha,"\n")
          pare
          caso 3:
            escreva ("\nFazendo Logout.....\n")
            escreva ("\nDigite o seu usúario: ")
            leia (usuario)
            escreva ("Digite a sua senha: ")
            leia (senha)
            se (usuario=="admin" e senha==password) {
              escreva ("\nAcesso Permitido!\n")
            }
            senao {
              
            }
          caso 4:
            escreva ("\nSaindo da conta. Muito Obrigado e Tenha um Bom Dia!")
          pare
          caso contrario:
            escreva ("\nOpção Invalida!\n")
        }
      }
    }
  }
}

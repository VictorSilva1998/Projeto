programa {
  funcao inicio() {

    inteiro choice,senha,password=1234,x=1,y=3
    cadeia usuario
    
    enquanto (x>0) {
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

          se (choice==1){ 
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
          }
          senao se (choice==2) {
            escreva ("\nNome do Usúario: ",usuario)
            escreva ("\nSenha do Usúario: ",senha,"\n")
          }
          senao se (choice==3) {
            escreva ("\nFazendo Logout.....\n\n")
          pare
          }
          senao se (choice==4) {
            x=0
            escreva ("\nSaindo da conta. Muito Obrigado e Tenha um Bom Dia!")
          pare
          }
          senao {
            escreva ("\nOpção Invalida!\n")
          }
        }
      }
    se (usuario!="admin" ou senha!=password) {
      escreva ("\nAcesso Negado\n\n")
    y=y-1
    }
    se (y==2) {
      escreva ("Você tem ",y," tentativas restantes. Você cometeu um erro. Acontece!\n\n")
    }
    se (y==1) {
      escreva ("Você tem ",y," tentativas restantes. Já errou 2 vezes. Toma cuidado!\n\n")
    }
    se (y==0) {
      escreva ("Você tem ",y," tentativas restantes. Limite de erros atingido. Desligando o Sistema.\n")
      escreva ("\nVocê é burro cara, que Loucura!\n")
    pare
    }
    }
  }
}
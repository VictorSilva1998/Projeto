lista = ["Carro", "Moto", "Casa"]

while True:
    print ("1 - Excluir Pedido")
    print ("0 - Sair")
    opcao = str (input ("Digite a opção desejada: "))

    if opcao == "1" and len (lista) > 0:
        excluir = str (input ("\nDigite o nome do produto que deseja excluir ou 0 para voltar: "))

        if excluir in lista:
            busca = lista.index (excluir)
            lista.pop (busca)
            print ("\nPedido Excluido!\n")
        
        elif excluir == "0":
            print ("\nVoltando...\n")
            opcao == "0"
        else:
            print ("\nPedido não encontrado!\n")
    
    elif opcao == "1" and len (lista) == 0:
        print ("\nNenhum pedido registrado!\n")
    
    elif opcao == "0":
        print ("\nVoltando para o Menu...\n")
        break
    
    else:
        print ("\nOpção Inválida!\n")
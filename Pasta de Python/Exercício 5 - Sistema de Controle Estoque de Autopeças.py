peca = []
codigo_lista = []
estoque = []
valores = []

while True:
    print ("========= Menu =========\n")
    print ("1 - Cadastrar Peça")
    print ("2 - Listar Estoque")
    print ("3 - Realizar Venda")
    print ("4 - Repor Estoque")
    print ("5 - Encerrar")
    opcao = str (input ("Digte a opção desejada: "))

    if opcao == "1":
        nome = str (input ("\nDigite o nome da peça: "))

        if nome in peca:
            print ("\nPeça já foi cadastrada. Se deseja repor o estoque utilize a opção 4 no Menu!\n")

        else:
            codigo = str (input ("Digite o código da peça: "))

            while True:
                try:
                    quantidade = int (input ("Digite a quantidade em estoque da peça: "))
                    break
                except ValueError:
                    print ("\nEntrada Inválida. Utilize apenas números inteiros. Por Favor!\n")
            
            while True:
                try:
                    valor = float (input ("Digite o valor unitário da peça: "))
                    break
                except ValueError:
                    print ("\nEntrada Inválida. Utilize apenas números inteiros ou decimais. Por Favor!\n")
            
            peca.append (nome)
            codigo_lista.append (codigo)
            estoque.append (quantidade)
            valores.append (valor)

            print ("\nPeça cadastrada com sucesso!\n")

    elif opcao == "2":
        if len (peca) > 0:
            for x in range (len (peca)):
                print ("\nNome da peça: %s, Estoque: %i." %(peca [x], estoque [x]))

        else:
            print ("\nNenhuma peça cadastrada!\n")

    elif opcao == "3":
        nome = str (input ("\nDigite o nome da peça que deseja vender: "))
        
        while True:
            if nome in peca:
                posicao = peca.index (nome)
                while True:
                    try:
                        venda = int (input ("Digite a quantidade que deseja vender da peça: "))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida. Utilize apenas números inteiros. Por Favor!\n")

                if venda > estoque [posicao]:
                    print ("\nExcede a quantidade da peça no estoque!\n")

                else:
                    custo = venda * valores [posicao]
                    restante = estoque [posicao] - venda
                    estoque [posicao] = restante
                    print ("\nVenda realizada com sucesso.")
                    print ("Valor da venda: R$ %.2f." %custo)
                    break

            else:
                print ("\nPeça não cadastrada!\n")
                break

    elif opcao == "4":
        nome = str (input ("\nDigite o nome da peça que deseja repor: "))

        while True:
            if nome in peca:
                posicao = peca.index (nome)
                while True:
                    try:
                        reposicao = int (input ("Digite a quantidade que deseja repor da peça: "))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida. Utilize apenas números inteiros. Por Favor!\n")

                novo = estoque [posicao] + reposicao
                estoque [posicao] = novo
                print ("\nPeça reposta com sucesso.")
                break

            else:
                print ("\nPeça não cadastrada!\n")
                break
    
    elif opcao == "5":
        print ("\nEncerrando...")
        break

    else:
        print ("\nOpção Inválida!\n")
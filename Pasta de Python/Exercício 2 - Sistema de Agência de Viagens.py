nomes = []
valores = []
vagas = []

while True:
    print ("========= Menu =========\n")
    print ("1 - Cadastrar destino turístico")
    print ("2 - Listar destinos disponíveis")
    print ("3 - Comprar passagem")
    print ("4 - Consultar vagas restantes")
    print ("5 - Encerrar sistema")
    opcao = str (input ("Digte a opção desejada: "))
    
    if opcao == "1":
        nome = str (input ("\nInforme o nome do destino: "))
        nomes.append (nome)

        while True:
            try:
                valor = float (input ("Informe o valor da passagem: "))
                valores.append (valor)
                break
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

        while True:
            try:
                quantidade = int (input ("Informe a quantidade de vagas disponíveis: "))
                vagas.append (quantidade)
                print ("\nDestino cadastrado com sucesso!\n")
                break
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números decimais. Por favor!\n")

    elif opcao == "2":
        try:
            print ("\nDestinos disponíveis: ", nomes,".\n")
        except ValueError:
            print ("\nNenhum destino cadastrado!\n")

    elif opcao == "3":
        destino = str (input ("\nDigite o destino turístico desejado: "))
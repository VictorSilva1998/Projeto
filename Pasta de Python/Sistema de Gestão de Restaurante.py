nome_lista = []
cidade_lista = []
estado_lista = []
funcionarios_lista = []
clientes_lista = []
faturamento_lista = []
entregues_lista = []
cancelados_lista = []
media_lista = []
cardapio_lista = []

while True:
    print ("===== Menu =====\n")
    print ("1 - Cadastro Restaurantes")
    print ("2 - Exibir Relatório Completo")
    print ("3 - Buscar Restaurante")
    print ("4 - Mostrar Estatísticas Gerais")
    print ("5 - Atualizar Dados de Restaurante")
    print ("6 - Remover Restaurante")
    print ("7- Sair\n")
    opcao = str (input ("Digte a opção desejada: "))
    
    if opcao == "1":
    
            y = int (input ("\nQuantas restaurantes deseja informar: "))

            for x in range (1, y + 1):
            
                print ("\nDigite as informações pedidas abaixo:\n")
                nome = str (input ("Nome do %i° Restaurante: " %x))
                cidade = str (input ("Cidade do %i° Restaurante: " %x))
                estado = str (input ("Estado do %i° Restaurante: " %x))

                while True:
                    try:
                        funcionarios = int (input ("Quantidade de funcionários do %i° Restaurante: " %x))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")

                while True:
                    try:
                        clientes = int (input ("Quantidade de clientes atendidos no mês do %i° Restaurante: " %x))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")
                
                while True:
                    try:
                        faturamento = float (input ("Faturamento Mensal do %i° Restaurante: " %x))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")
                
                while True:
                    try:
                        entregues = int (input ("Quantidade de pedidos entregues do %i° Restaurante: " %x))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")
                
                while True:
                    try:
                        cancelados = int (input ("Quantidade de pedidos cancelados do %i° Restaurante: " %x))
                        break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")

                while True:
                    try:
                        while True:
                            media = float (input ("Nota média dos clientes do %i° Restaurante: " %x))

                            if media < 0 or media > 10:
                                    print ("\nA média deve ser um valor de 0 a 10!\n")
                            else:
                                media_lista.append (media)
                                break
                    except ValueError:
                        print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

                    while True:
                        try:
                            cardapio = int (input ("Quantidade de pratos no cardápio do %i° Restaurante: " %x))
                            break
                        except ValueError:
                            print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")

                    nome_lista.append (nome)
                    cidade_lista.append (cidade)
                    estado_lista.append (estado)
                    funcionarios_lista.append (funcionarios)
                    clientes_lista.append (clientes)
                    faturamento_lista.append (faturamento)
                    entregues_lista.append (entregues)
                    cancelados_lista.append (cancelados)
                    cardapio_lista.append (cardapio)

                    print ("\nRestaurante Cadastrado!\n")
                    break
    
    elif opcao == "2":

            print ("\n========== Relatório ==========\n")

            try:       
                mais_de_100 = [num for num in cardapio_lista if num > 100]
                pratos = cardapio_lista.index (mais_de_100)
                print ("Restaurantes que possuem mais de 100 pratos no cardapio: ", nome_lista [pratos])
                break
            except ValueError:
                print ("Nenhum restaurante cadastrado possui mais de 100 pratos!")

                try:
                    mais_de_9 = [num for num in media_lista if num > 9]
                    media_alta = media_lista.index (mais_de_9)
                    print ("Restaurantes que tiveram nota média acima de 9: ", nome_lista [media_alta])
                except ValueError:
                    print ("Nenhum restaurante cadastrado teve nota média acima de 9!")

                    try:
                        atendidos_max = max (clientes_lista)
                        atendidos_mais = clientes_lista.index (atendidos_max)
                        print ("Restaurante com maior quantidade de clientes atendidos: ", nome_lista [atendidos_mais])
                    except ValueError:
                        print ("Nenhum restaurante cadastrado!")

                    try:  
                        mais_de_100000 = [num for num in faturamento_lista if num > 100000]
                        super_faturamento = faturamento_lista.index (mais_de_100000)
                        print ("Restaurantes cujo faturamento ultrapassa R$ 100.000,00: ", nome_lista [super_faturamento])
                    except ValueError:
                        print ("Nenhum restaurante cadastrado possui faturamento ultrapassa de R$ 100.000,00!\n")


    elif opcao == "3":
            nome_consulta = str (input ("\nDigite o nome do restaurante desejado: "))

            if nome_consulta in nome_lista:
                indice = nome_lista.index (nome_consulta)

                print ("\nNome: ", nome_lista [indice])
                print ("Cidade: ", cidade_lista [indice])
                print ("Estado: ", estado_lista [indice])
                print ("Funcionários: ", funcionarios_lista [indice])
                print ("Clientes no mês: ", clientes_lista [indice])
                print ("Faturamento: %.2f" %faturamento_lista [indice])
                print ("Pedidos entregues: ", entregues_lista [indice])
                print ("Pedidos cancelados: ", cancelados_lista [indice])
                print ("Nota Média dos Clientes: %.2f" %media_lista [indice])
                print ("Quantidade de pratos no cardápio: ", cardapio_lista [indice],"\n")

            else:
                print ("\nNome não Encontrado!\n")

    elif opcao == "4":
        
        print ("\n========== Estatísticas ==========\n")

        try:
            faturamento_media = (sum (faturamento_lista)) / (len (faturamento_lista))
            nomes_selecionados = [nome_lista[i] for i, valor in enumerate(faturamento_lista) if valor > faturamento_media]
            print ("Restaurantes que possuem faturamento acima da média geral: ", nomes_selecionados)
        except ValueError:
            print ("Nenhum restaurante cadastrado!")
            
        try:
            soma_faturamento_estados = {}

            for nomes, valor in zip(nome_lista, faturamento_lista):
                if nomes in soma_faturamento_estados:
                    soma_faturamento_estados[nomes] += valor
                else:
                    soma_faturamento_estados[nomes] = valor

            nome_maior_soma = max(soma_faturamento_estados, key=soma_faturamento_estados.get)
            maior_valor = soma_faturamento_estados[nome_maior_soma]
            print ("Estado com maior faturamento total: ", nome_maior_soma,", com um total de", maior_valor,".")
        except ValueError:
            print ("Nenhum restaurante cadastrado!")

        print ("Cidade com mais clientes atendidos: ", nome_lista [super_faturamento])
        print ("Porcentagem de restaurantes  com nota superior a 8: ", nome_lista [super_faturamento])
        print ("Total geral de pedidos cancelados: %i" %sum (cancelados_lista))
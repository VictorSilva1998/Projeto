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
    print ("===== Menu =====")
    print ("1 - Cadastro Restaurantes")
    print ("2 - Exibir Relatório Completo")
    print ("3 - Buscar Restaurante")
    print ("4 - Mostrar Estatísticas Gerais")
    print ("5 - Atualizar Dados de Restaurante")
    print ("6 - Remover Restaurante")
    print ("7- Sair")
    opcao = str (input ("Digte a opção desejada: "))
    
    if opcao == "1":
    
            y = int (input ("Quantas restaurantes deseja informar: "))

            for x in range (y):
            
                print ("\nDigite as informações pedidas abaixo:\n")
                nome = str (input ("Nome do %i° Restaurante: " %x))
                cidade = str (input ("Cidade do %i° Restaurante: " %x))
                estado = str (input ("Estado do %i° Restaurante: " %x))
                funcionarios = int (input ("Quantidade de funcionários do %i° Restaurante: " %x))
                clientes = int (input ("Quantidade de clientes atendidos no mês do %i° Restaurante: " %x))
                faturamento = float (input ("Faturamento Mensal do %i° Restaurante: " %x))
                entregues = int (input ("Quantidade de pedidos entregues do %i° Restaurante: " %x))
                cancelados = int (input ("Quantidade de pedidos cancelados do %i° Restaurante: " %x))
                media = float (input ("Nota média dos clientes do %i° Restaurante: " %x))
                cardapio = int (input ("Quantidade de pratos no cardápio do %i° Restaurante: " %x))

                nome_lista.append (nome)
                cidade_lista.append (cidade)
                estado_lista.append (estado)
                funcionarios_lista.append (funcionarios)
                clientes_lista.append (clientes)
                faturamento_lista.append (faturamento)
                entregues_lista.append (entregues)
                cancelados_lista.append (cancelados)
                media_lista.append (media)
                cardapio_lista.append (cardapio)

                print ("\nRestaurante Cadastrado!\n")
    
    elif opcao == "2":
         
        mais_de_100 = [num for num in cardapio_lista if num > 100]
        pratos = cardapio_lista.index (mais_de_100)

        mais_de_9 = [num for num in media_lista if num > 9]
        media_alta = media_lista.index (mais_de_9)

        atendidos_max = max (clientes_lista)
        atendidos_mais = clientes_lista.index (atendidos_max)

        mais_de_100000 = [num for num in faturamento_lista if num > 100000]
        super_faturamento = faturamento_lista.index (mais_de_100000)

        print ("Restaurantes que possuem mais de 100 pratos no cardapio: ", nome_lista [pratos])
        print ("Restaurantes que tiveram nota média acima de 9: ", nome_lista [media_alta])
        print ("Restaurante com maior quantidade de clientes atendidos: ", nome_lista [atendidos_mais])
        print ("Restaurantes cujo faturamento ultrapassa R$ 100.000,00: ", nome_lista [super_faturamento])
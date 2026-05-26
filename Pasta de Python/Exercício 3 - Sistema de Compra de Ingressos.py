nome = str (input ("Informe o seu nome: "))
quantidade_lista = [0, 0, 0]
total_lista = [0, 0, 0]

while True:
    print ("========= Menu =========\n")
    print ("1 - Comprar Ingressos")
    print ("2 - Resumo de Todas as Compras")
    print ("3 - Encerrar")
    opcao = str (input ("Digte a opção desejada: "))

    if opcao == "1":
        print ("\nTipos de Ingressos:\n")
        print ("1 - Pista")
        print ("2 - VIP")
        print ("3 - Camarote")

        while True:
            try:
                tipo = str (input ("\nInforme o tipo de ingresso desejado: "))

                if tipo == "1":
                    valor = 50
                    local = 0
                    break
                
                elif tipo == "2":
                    valor = 120
                    local = 1
                    break
                
                elif tipo == "3":
                    valor = 250
                    local = 2
                    break

                else:
                    print ("\nOpção Inválida!")
                
            except ValueError:
                print ("\nInválido! Utilize os números 1, 2 ou 3 para escolher o tipo de ingresso. Por Favor!\n")


        while True:
            try:
                quantidade = int (input ("Informe a quantidade de ingressos desejados: "))
                break
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números decimais. Por favor!\n")

        print ("\nResumo da compra:")
        print ("Cliente: %s." %nome)
        print ("Tipo de Ingressos comprados: %s." %tipo)
        print ("Quantidade de Ingressos comprados: %i." %quantidade)
        total = quantidade * valor
        resultado = total + total_lista [local]
        total_lista [local] = resultado
        quantidade_total = quantidade + quantidade_lista [local]
        quantidade_lista [local] = quantidade_total
        print ("Total da Compra: %i.\n" %total)

    elif opcao == "2":
        print ("\n========= Resumo =========\n")
        print ("Pista: %i, total comprado: %.2f" %(quantidade_lista [0], total_lista [0]))
        print ("VIP: %i, total comprado: %.2f" %(quantidade_lista [1], total_lista [1]))
        print ("Camarote: %i, total comprado: %.2f" %(quantidade_lista [2], total_lista [2]))
        print ("Total comprado: %.2f.\n" %sum (total_lista))
    
    elif opcao == "3":
        print ("\nEncerrando...")
        break

    else:
        print ("\nOpção Inválida!\n")
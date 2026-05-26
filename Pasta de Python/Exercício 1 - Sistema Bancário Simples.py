nome_lista = []
saldo_lista = []

while True:
    print ("========= Menu =========\n")
    print ("1 - Cadastro")
    print ("2 - Login")
    print ("3 - Sair")
    opcao = str (input ("Digte a opção desejada: "))

    if opcao == "1":
        nome = str (input ("Informe o seu nome: "))
        nome_lista.append (nome)

        while True:
            try:
                saldo = float (input ("Informe o saldo inicial da conta: "))
                print ("Cadastro realizado com sucesso!\n")
                saldo_lista.append (saldo)
                break
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

    elif opcao == "2":
        nome_login = str (input ("Digite o seu nome: "))

        if nome_login in nome_lista:
            while True:
                local_nome = nome_lista.index (nome_login)
                print ("\n========= Menu do Banco =========\n")
                print ("1 - Deposito")
                print ("2 - Saque")
                print ("3 - Saldo")
                print ("4 - Voltar")
                escolha = str (input ("Digite a opção desejada: "))

                if escolha == "1":
                    while True:
                        try:
                            deposito = float (input ("Digite o valor que deseja depositar: "))
                            resultado = deposito + (saldo_lista [local_nome])
                            saldo_lista [local_nome] = resultado
                            print ("\nDepósito realizado com sucesso!")
                            break
                        except ValueError:
                            print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

                elif escolha == "2":
                    while True:
                        try:
                            saque = float (input ("Digite o valor que deseja sacar: "))

                            if saque < saldo_lista [local_nome]:
                                resultado = (saldo_lista [local_nome]) - saque
                                saldo_lista [local_nome] = resultado
                                print ("\nSaque realizado com sucesso!")
                                break
                            
                            else:
                                print ("\nSaldo Insuficiente!\n")

                        except ValueError:
                            print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

                elif escolha == "3":
                    print ("\nSaldo da conta %.2f.\n" %saldo_lista [local_nome])

                elif escolha == "4":
                    print ("\nVoltando...\n")
                    break

                else:
                    print ("\nOpção inválida!\n")

        else:
            print ("\nNome não cadastrado!\n")

    elif opcao == "3":
        print ("\nSaindo!\n")
        break

    else:
        print ("\nOpção Inválida!\n")
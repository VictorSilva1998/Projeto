nome_gerente = "1234"
senha_gerente = "1234"
nome_lista = []
endereco_lista = []
telefone_lista = []
cpf_lista = []
agencia_lista = []
conta_lista = []
saldo_lista = []
email_lista = []
nascimento_lista = []
tipo_lista = []
senha_lista = []
limite_lista = []

print ("===== Login =====")
print ("Informe as informações abaixo:")
nome_login = str (input ("Usuário: "))
senha_login = str (input ("Senha: "))

if nome_login == nome_gerente and senha_login == senha_gerente:
    print ("\nBem-Vindo!\n")
    while True:
        print ("===== Menu =====")
        print ("1 - Cadastro de Cliente")
        print ("2 - Consulta de Cadastro")
        print ("3 - Exclusão de Cadastro")
        print ("4 - Ver Saldo")
        print ("5 - Depósito")
        print ("6 - Saque")
        print ("7- Sair")
        opcao = str (input ("Digte a opção desejada: "))

        if opcao == "1":
    
            print ("\nDigite as informações pedidas abaixo:\n")
            nome = str (input ("Nome: "))
            endereco = str (input ("Endereço: "))
            telefone = str(input("Telefone: "))
            cpf = str(input("CPF: "))
            agencia = str(input("Agência: "))
            conta = str(input("Número da Conta: "))
            saldo = float (input("Saldo: "))
            email = str(input("Email: "))
            nascimento = str(input("Data de Nascimento: "))
            tipo = str(input("Tipo de Conta: "))
            senha = str(input("Senha: "))
            limite = str(input("Limite de Crédito: "))

            nome_lista.append (nome)
            endereco_lista.append (endereco)
            telefone_lista.append (telefone)
            cpf_lista.append (cpf)
            agencia_lista.append (agencia)
            conta_lista.append (conta)
            saldo_lista.append (saldo)
            email_lista.append (email)
            nascimento_lista.append (nascimento)
            tipo_lista.append (tipo)
            senha_lista.append (senha)
            limite_lista.append (limite)

            print ("\nCliente Cadastrado!\n")
        
        elif opcao == "2":
            cpf_consulta = str (input ("\nDigite o CPF do cliente desejado: "))

            if cpf_consulta in cpf_lista:
                indice = cpf_lista.index (cpf_consulta)

                print ("\nNome: ", nome_lista [indice])
                print ("Endereço: ", endereco_lista [indice])
                print ("Telefone: ", telefone_lista [indice])
                print ("CPF: ", cpf_lista [indice])
                print ("Agência: ", agencia_lista [indice])
                print ("Conta: ", conta_lista [indice])
                print ("Saldo: ", saldo_lista [indice])
                print ("E-mail: ",email_lista [indice])
                print ("Data de Nascimento: ", nascimento_lista [indice])
                print ("Tipo de Conta: ", tipo_lista [indice])
                print ("Limite de Crédito: ", limite_lista [indice], "\n")

            else:
                print ("\nCPF não Encontrado!\n")

        elif opcao == "3":
            cpf_excluir = str (input ("\nDigite o CPF do cliente desejado: "))
            
            if cpf_excluir in cpf_lista:
                indice = cpf_lista.index (cpf_excluir)

                nome_lista.pop (indice)
                endereco_lista.pop (indice)
                telefone_lista.pop (indice)
                cpf_lista.pop (indice)
                agencia_lista.pop (indice)
                conta_lista.pop (indice)
                saldo_lista.pop (indice)
                email_lista.pop (indice)
                nascimento_lista.pop (indice)
                tipo_lista.pop (indice)
                senha_lista.pop (indice)
                limite_lista.pop (indice)

                print ("\nDados excluídos com sucesso!\n")

            else:
                print ("\nCPF não Encontrado!\n")
        
        elif opcao == "4":
            conta_saldo = str (input ("\nDigite o número da conta desejada: "))

            if conta_saldo in conta_lista:
                indice = conta_lista.index (conta_saldo)

                senha_saldo = str (input ("\nDigite a senha: "))

                if senha_saldo in senha_lista [indice]:
                    print ("Saldo da Conta: %.2f" %saldo_lista [indice])

                else:
                    print ("\nSenha Incorreta!\n")

            else:
                print ("\nConta não encontrada!\n")

        elif opcao == "5":
            conta_deposito = str (input ("\nDigite o número da conta desejada: "))

            if conta_deposito in conta_lista:
                indice = conta_lista.index (conta_deposito)

                deposito = float (input ("Digite o valor que deseja depositar: "))

                saldo_deposito = saldo_lista [indice] + deposito

                saldo_lista [indice] = saldo_deposito
            
            else:
                print ("\nConta não encontrada!\n")
        
        elif opcao == "6":
            conta_saque = str (input ("\nDigite o número da conta desejada: "))

            if conta_saque in conta_lista:
                indice = conta_lista.index (conta_saque)

                senha_saque = str (input ("Digite a senha: "))

                if senha_saque == senha_lista [indice]:

                    saque = float (input ("Digite o valor que deseja sacar: "))

                    if saque < saldo_lista [indice]:

                        saldo_saque = saldo_lista [indice] - saque

                        saldo_lista [indice] = saldo_saque

                        print ("\nSaque Realizado com Sucesso!\n")

                    else:
                        print ("\nSaldo Insuficiente!\n")
                    
                else:
                    print ("\nSenha Incorreta!\n")

            else:
                print ("\nConta não encontrada!\n")
            
        elif opcao == "7":
            print ("\nSaindo...\n")
            break

        else:
            print ("\nOpção Inválida!\n")
    
else:
    print ("\nUsuário/Senha Incorretos!\n")
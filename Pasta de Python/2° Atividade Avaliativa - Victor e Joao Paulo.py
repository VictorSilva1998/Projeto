nome_gerente = "1234"
senha_gerente = "1234"
escolha = "1"
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
        print ("4 - Editar Clientes")
        print ("5 - Ver Saldo")
        print ("6 - Depósito")
        print ("7 - Saque")
        print ("8 - Sair")
        opcao = str (input ("Digte a opção desejada: "))

        if opcao == "1":
    
            print ("\nDigite as informações pedidas abaixo:\n")
            nome = str (input ("Nome: "))
            endereco = str (input ("Endereço: "))
            telefone = str(input("Telefone: "))
            cpf = str(input("CPF: "))
            agencia = str(input("Agência: "))
            conta = str(input("Número da Conta: "))

            while True:
                try:
                    saldo = float (input("Saldo: "))
                    break
                except ValueError:
                    print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")
                    
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
                print ("Saldo: %.2f" %saldo_lista [indice])
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
            editar = str (input ("\nDigite o CPF do cliente desejado: "))

            if editar in cpf_lista:
                indice = cpf_lista.index (editar)

                while escolha != "0":

                    print ("\n1 - Nome")
                    print ("2 - Endereço")
                    print ("3 - Telefone")
                    print ("4 - CPF")
                    print ("5 - Agência")
                    print ("6 - Número da Conta")
                    print ("7 - E-mail")
                    print ("8 - Data de Nascimento")
                    print ("9 - Tipo de Conta")
                    print ("10 - Senha")
                    print ("11 - Limite de Crédito")
                    print ("0 - Voltar")
                    escolha = str (input ("Digite a opção desejada acima: "))

                    if escolha == "1":
                        novo_nome = str (input ("\nDigite o novo nome: "))

                        nome_lista [indice] = novo_nome
                        print ("\nNome Editado com Sucesso!\n")

                    elif escolha == "2":
                        novo_endereco = str (input ("\nDigite o novo endereço: "))

                        endereco_lista [indice] = novo_endereco
                        print ("\nEndereço Editado com Sucesso!\n")

                    elif escolha == "3":
                        novo_telefone = str (input ("\nDigite o novo telefone: "))

                        telefone_lista [indice] = novo_telefone
                        print ("\nTelefone Editado com Sucesso!\n")

                    elif escolha == "4":
                        novo_cpf = str (input ("\nDigite o novo cpf: "))

                        cpf_lista [indice] = novo_cpf
                        print ("\nCPF Editado com Sucesso!\n")

                    elif escolha == "5":
                        novo_agencia = str (input ("\nDigite a nova agência: "))

                        agencia_lista [indice] = novo_agencia
                        print ("\nAgência Editada com Sucesso!\n")

                    elif escolha == "6":
                        novo_conta = str (input ("\nDigite o novo número da conta: "))

                        conta_lista [indice] = novo_conta
                        print ("\nNúmero da Conta Editado com Sucesso!\n")

                    elif escolha == "7":
                        novo_email = str (input ("\nDigite o novo e-mail: "))

                        email_lista [indice] = novo_email
                        print ("\nE-mail Editado com sucesso!\n")

                    elif escolha == "8":
                        novo_nascimento = str (input ("\nDigite a nova Data de Nascimento: "))

                        nascimento_lista [indice] = novo_nascimento
                        print ("\nData de Nascimento Editada com sucesso!\n")

                    elif escolha == "9":
                        novo_tipo = str(input ("\nDigite o novo tipo da conta: "))

                        tipo_lista [indice] = novo_tipo
                        print("\nTipo da Conta Editado com Sucesso!")

                    elif escolha == "10":
                        nova_senha = str (input ("\nDigite a nova senha: "))

                        senha_lista [indice] = nova_senha
                        print ("\n Senha Editada com Sucesso!")

                    elif escolha == "11":
                        novo_limite = str (input ("\nDigite o novo limite de crédito: "))

                        limite_lista [indice] = novo_limite
                        print ("\nLimite de Crédito Editado com Sucesso!\n")

                    elif escolha == "0":
                        print ("\nRetornando...\n")

                    else:
                        print ("\nOpção Inválida!\n")

            else:
                print ("\nCPF não Encontrado!\n")

        elif opcao == "5":
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

        elif opcao == "6":
            conta_deposito = str (input ("\nDigite o número da conta desejada: "))

            if conta_deposito in conta_lista:
                indice = conta_lista.index (conta_deposito)

                while True:
                    try:
                        deposito = float (input ("Digite o valor que deseja depositar: "))

                        saldo_deposito = saldo_lista [indice] + deposito

                        saldo_lista [indice] = saldo_deposito
                        break

                    except ValueError:
                        print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")
            
            else:
                print ("\nConta não encontrada!\n")
        
        elif opcao == "7":
            conta_saque = str (input ("\nDigite o número da conta desejada: "))

            if conta_saque in conta_lista:
                indice = conta_lista.index (conta_saque)

                senha_saque = str (input ("Digite a senha: "))

                if senha_saque == senha_lista [indice]:
                    
                    while True:
                        try:
                            saque = float (input ("Digite o valor que deseja sacar: "))
                            break

                        except ValueError:
                            print ("\nEntrada Inválida! Utilize números decimais. Por favor!\n")

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
            
        elif opcao == "8":
            print ("\nSaindo...\n")
            break

        else:
            print ("\nOpção Inválida!\n")
    
else:
    print ("\nUsuário/Senha Incorretos!\n")
import copy

ano_2026 = [["Victor", "Vinicius", "João"] , [20, 15, 10] , [3000.00, 2500.00, 2000.00]]
ano_2027 = copy.deepcopy(ano_2026)

while True:
    print ("1 - Atualizar dados")
    print ("0 - Sair")
    opcao = str (input ("Digite a opção desejada: "))

    if opcao == "1":
        nome = str (input ("\nDigite o nome do funcionário desejado: "))

        if nome in ano_2026[0]:
            local = ano_2026[0].index (nome)
            while True:
                try:
                    tarefas = int (input ("\nQuantas tarefas foram feitas em 2027: "))
                    ano_2027 [1] [local] = tarefas
                    break

                except ValueError:
                    print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

            while True:
                try:
                    salario = float (input ("\nQual o salário dele em 2027: "))
                    ano_2027 [2] [local] = salario
                    break

                except ValueError:
                    print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

            print ("\nAtualizado com sucesso!\n")

        else:
            print ("\nNome não encontrado!")

    elif opcao == "0":
        print ("\nSaindo...")
        break

    else:
        print ("\nOpção Inválida!\n")
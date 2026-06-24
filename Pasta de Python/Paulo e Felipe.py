import copy

ano_2026 = [["Victor", "Vinicius", "João"] , [20, 15, 10] , [3000.00, 2500.00, 2000.00]]
ano_2027 = copy.deepcopy(2026)

while True:
    print ("1 - Atualizar dados")
    print ("0 - Sair")
    opcao = str (input ("Digite a opção desejada: "))

    if opcao == "1":
        nome = str (input ("\nDigite o nome do funcionário desejado: "))

        if nome in ano_2026[0]:
            local = ano_2026[0].index (nome)
            tarefas = str (input ("Quantas tarefas foram feitas em 2027: "))
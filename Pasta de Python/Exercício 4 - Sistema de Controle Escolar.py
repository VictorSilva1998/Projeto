nome_lista = []
nota1_lista = []
nota2_lista = []

while True:
    print ("========= Menu =========\n")
    print ("1 - Cadastrar Aluno")
    print ("2 - Listar Alunos")
    print ("3 - Consultar Situação Individual")
    print ("4 - Encerrar")
    opcao = str (input ("Digte a opção desejada: "))

    if opcao == "1":
        nome = str (input ("\nDigite o nome do aluno: "))

        while True:
            try:
                nota1 = float (input ("Digite a 1ª nota do aluno: "))

                if nota1 < 0 or nota1 > 10:
                    print ("\nNota Inválida. Devem ser um valor de 0 à 10!\n")
                else:
                    break

            except ValueError:
                print ("\nValor Inválido. Ultilize apenas números!\n")

        while True:
            try:
                nota2 = float (input ("Digite a 2ª nota do aluno: "))

                if nota2 < 0 or nota2 > 10:
                    print ("\nNota Inválida. Devem ser um valor de 0 à 10!")
                else:
                    break

            except ValueError:
                print ("\nValor Inválido. Ultilize apenas números!\n")

        nome_lista.append (nome)
        nota1_lista.append (nota1)
        nota2_lista.append (nota2)

        print ("\nAluno cadastrado com sucesso!\n")

    elif opcao == "2":
        print ("Lista de alunos: ", nome_lista,".\n")

    elif opcao == "3":
        consulta = str (input ("\nDigite o nome do aluno desejado: "))

        if consulta in nome_lista:
            posicao = nome_lista.index (consulta)
            media = (nota1_lista [posicao] + nota2_lista [posicao]) / 2

            if media >= 7:
                print ("\nAluno Aprovado!\n")

            elif media >= 5 and media <= 6.9:
                print ("\nAluno de Recuperação!\n")

            elif media < 5:
                print ("\nAluno Aprovado!\n")

        else:
            print ("\nNome não cadastrado!\n")
    
    elif opcao == "4":
        print ("\nEncerrando...")
        break

    else:
        print ("\nOpção Inválida!\n")
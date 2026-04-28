escolha = 1
lista = []

while escolha != "0":

    print ("===== Menu =====")
    print ("1 - Cadastro")
    print ("2 - Consulta")
    print ("3 - Excluir Cliente")
    print ("0 - Sair")
    escolha = str (input ("Selecione uma das opções acima: "))

    if escolha == "1":
        nome = str (input ("\nDigite o nome do novo cliente: "))
        print ("\nMatricula realizada!\n")
        lista.append (nome)
    elif escolha == "2":
        matricula = int (input ("\nDigite o numero da matricula do cliente desejado: "))
        print ("\nCliente: ", lista[matricula],"\n")
    elif escolha == "3":
        excluir = int (input ("\nDigite o número da matricula do cliente que deseja deletar: "))
        lista.pop (excluir)
        print ("\nCliente Excluido!\n")
    elif escolha == "0":
        print ("\nSaindo...")
    else:
        print ("\nOpção Inválida!\n")
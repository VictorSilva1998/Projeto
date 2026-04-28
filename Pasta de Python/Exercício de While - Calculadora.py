escolha = 1

while escolha !=0:
    print ("----- Calculadora -----")
    print ("1 - Multiplicação")
    print ("2 - Divisão")
    print ("3 - Adição")
    print ("4 - Subtração")
    print ("0 - Sair")
    escolha = int (input ("Escolha uma das opções acima: "))

    if escolha == 1:
        x = float (input ("\nDigite o primeiro número da operação: "))
        y = float (input ("Digite o segundo número da operação: "))
        total = x * y
        print ("\nResposta: %.2f\n" %total)
        continue
    elif escolha == 2:
        x = float (input ("\nDigite o primeiro número da operação: "))
        y = float (input ("Digite o segundo número da operação: "))
        total = x / y
        print ("\nResposta: %.2f\n" %total)
        continue
    elif escolha == 3:
        x = float (input ("\nDigite o primeiro número da operação: "))
        y = float (input ("Digite o segundo número da operação: "))
        total = x + y
        print ("\nResposta: %.2f\n" %total)
        continue
    elif escolha == 4:
        x = float (input ("\nDigite o primeiro número da operação: "))
        y = float (input ("Digite o segundo número da operação: "))
        total = x - y
        print ("\nResposta: %.2f\n" %total)
        continue
    elif escolha > 4 or escolha < 0:
        print ("\nOpção Invalida!\n")
        continue
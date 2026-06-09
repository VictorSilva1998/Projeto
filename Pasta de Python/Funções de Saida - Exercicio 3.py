def horario (horas, minutos):
    if horas > 12 and horas < 24:
        resultado = horas - 12
        print ("\nHoras:", resultado,":", minutos,"P.M\n")

    elif horas >= 0 and horas <= 12:
        print ("\nHoras:", horas,":", minutos,"A.M\n")
    
    else:
        print ("\nHoras:", horas,":", minutos,"A.M\n")

while True:
    print ("1 - Converter Horas")
    print ("0 - Sair")
    opcao = input ("Digite a opção desejada: ")

    if opcao == "1":
        while True:
            try:
                entrada = int (input ("\nDigite as horas: "))

                if entrada >=0 and entrada <= 23:
                    break

                else:
                    print ("\nO valor de ser um número de 0 á 23.\n")
            
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

        while True:
            try:
                entradaMin = int (input ("\nDigite os minutos: "))

                if entradaMin >=0 and entradaMin <= 59:
                    break

                else:
                    print ("\nO valor de ser um número de 0 á 59.\n")
            
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

        horario (entrada, entradaMin)

    elif opcao == "0":
        print ("\nSaindo...")
        break

    else:
        print ("\nOpção Inválida!\n")
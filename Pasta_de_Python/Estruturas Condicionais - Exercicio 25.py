print ("1 - Soma de 2 números.")
print ("2 - Diferença de 2 números (maior pelo menor).")
print ("3 - Produto entre 2 números.")
print ("4 - Divisão entre 2 números.")
opcao = int (input ("Escolha a opção: "))


if opcao == 1:
    x = float (input ("Digite o primeiro número: "))
    y = float (input ("Digite o segundo número: "))
    resultado = x + y
    print (resultado)
elif opcao == 2:
    x = float (input ("Digite o primeiro número: "))
    y = float (input ("Digite o segundo número: "))
    if x > y:
        resultado = x - y
        print (resultado)
    else:
        resultado = y - x
        print (resultado)
elif opcao == 3:
    x = float (input ("Digite o primeiro número: "))
    y = float (input ("Digite o segundo número: "))
    resultado = x * y
    print (resultado)
elif opcao == 4:
    x = float (input ("Digite o primeiro número: "))
    y = float (input ("Digite o segundo número: "))
    resultado = x / y
    print (resultado)
else:
    print ("Opção Inválida")
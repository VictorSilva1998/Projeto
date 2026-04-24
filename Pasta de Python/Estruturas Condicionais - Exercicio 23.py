print ("----- Calculadora -----")
print ("1 - Adição")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")
opcao = int (input ("Escolha uma das opções acima:"))
x = float (input ("Digite o primeiro número: "))
y = float (input ("Digite o segundo número: "))

if opcao == 1:
    resultado = x + y
    print (resultado)
elif opcao == 2:
    resultado = x - y
    print (resultado)
elif opcao == 3:
    resultado = x * y
    print (resultado)
elif opcao == 4:
    resultado = x / y
    print (resultado)
else:
    print ("Opção Invalida")
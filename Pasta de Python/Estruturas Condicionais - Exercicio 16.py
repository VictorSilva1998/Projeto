salario = float (input ("Digite o valor do salário do Seu João: "))
emprestimo = float (input ("Digite o valor da prestação do empréstimo do Seu João: "))

prestacao = salario * 1.2

if emprestimo > prestacao:
    print ("Empréstimo não concedido.")
else:
    print ("Empréstimo concedido.")
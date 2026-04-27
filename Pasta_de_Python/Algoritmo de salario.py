salario = float (input ("Digite o valor do salário do funcionário: "))

if salario < 500:
    total = salario * 1.15
    print ("%.2f" %total)
elif salario >= 500 and salario <=1000:
    total = salario * 1.1
    print ("%.2f" %total)
else:
    total = salario * 1.05
    print ("%.2f" %total)
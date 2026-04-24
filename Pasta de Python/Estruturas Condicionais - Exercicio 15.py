horas = float (input ("Digite o número de horas trabalhadas pelo funcionário: "))

salario = 40.50 * horas

if salario > 2500:
    salario_liquido = salario * 0.89
    print ("Salário do funcionário: %.2f." %salario_liquido)
else:
    print ("Salário do funcionário: %.2f." %salario)
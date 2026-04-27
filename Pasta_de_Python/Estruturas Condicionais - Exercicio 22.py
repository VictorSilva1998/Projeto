b1 = float (input ("Digite o valor da base maior do trapézio: "))
b2 = float (input ("Digite o valor da base menor do trapézio: "))
altura = float (input ("Digite o valor da altura do trapézio: "))

if b1 > 0 and b2 > 0:
    a = ((b1 + b2) * altura) / 2
    print (a)
else:
    print ("Valor das bases deve ser maior que 0.")
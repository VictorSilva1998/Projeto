x = float (input ("Digite o valor de aquisição do produto: "))

if x < 50:
    venda=x*1.45
    print ("O valor de venda do produto será de %.2f" %venda)
else:
    venda=x*1.3
    print ("O valor de venda do produto será de %.2f" %venda)
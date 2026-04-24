produto1 = float (input ("Digite o valor do primeiro produto: "))
produto2 = float (input ("Digite o valor do segundo produto: "))
produto3 = float (input ("Digite o valor do terceiro produto: "))
produto4 = float (input ("Digite o valor do quarto produto: "))
produto5 = float (input ("Digite o valor do quinto produto: "))

vista = (produto1+produto2+produto3+produto4+produto5)*0.9
cartao = (produto1+produto2+produto3+produto4+produto5)*0.95
parcelado = produto1+produto2+produto3+produto4+produto5

print (f"Valor à vista = 10% desconto =  {vista:.2f}")
print (f"Valor no cartão = 5% desconto = {cartao:.2f}")
print ("Valor parcelado = sem desconto = %.2f" % parcelado)
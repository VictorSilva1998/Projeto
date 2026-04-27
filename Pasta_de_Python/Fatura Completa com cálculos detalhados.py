nome = input ("Digite o seu nome: ")
produto1 = float (input ("Digite o valor do primeiro produto: "))
produto2 = float (input ("Digite o valor do segundo produto: "))
produto3 = float (input ("Digite o valor do terceiro produto: "))

total = produto1+produto2+produto3
media = total/3
imposto = total/0.88
desconto = imposto*0.95

print ("\nCliente: %s" %nome)
print ("Média dos Preços: %.2f" %media)
print ("Valor com imposto: %.2f" %imposto)
print ("Valor com desconto: %.2f" %desconto)
print ("Total da compra: %.2f" %total)
produto = str (input ("Digite o nome do produto: "))
quantidade = int (input ("Digite a quantidade do produto a ser comprada: "))
valor = float (input ("Digite o valor unitario do produto: "))
desconto = int (input ("Digite o valor do desconto a ser aplicado para o pagamento: "))

total = (valor*quantidade)*((100-desconto)/100)

print ("\nProduto: %s" %produto)
print ("Valor Total da venda: R$ %.2f" %total)
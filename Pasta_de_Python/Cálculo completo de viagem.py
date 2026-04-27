distancia = float (input ("Digite o valor da distância total: "))
consumo = float (input ("Digite o valor do consumo de combustível do carro: "))
preco = float (input ("Digite o valor do preço do combustível: "))

l_necessarios=consumo*distancia
custo=l_necessarios*preco

print ("\nLitros necessários para a viagem: %.2f" %l_necessarios)
print ("Custo total da viagem: %.2f" %custo)
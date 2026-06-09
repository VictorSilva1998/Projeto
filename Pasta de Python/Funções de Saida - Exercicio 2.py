def somaImposto(taxaImposto, custo):
    Imposto = (custo * taxaImposto) / 100
    total = custo + Imposto
    print ("O custo da venda é de R$", custo,", com uma taxa de", porcentagem,"%, resultando num total de R$", Imposto,"de imposto e um total de venda de R$", total,".")
    return Imposto

while True:
    try:
        valor = float (input ("Digite o valor da compra: "))
        break
    except ValueError:
        print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

while True:
    try:
        porcentagem = float (input ("Digite a porcentagem do imposto: "))
        break
    except ValueError:
        print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")
        
somaImposto (porcentagem, valor)
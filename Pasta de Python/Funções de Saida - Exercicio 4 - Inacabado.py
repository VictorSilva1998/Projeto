parcela = 0
x = 0
y = 0
total = 0
cobrado = 0

def valorPagamento (prestacao, atraso):
    while True:

        if prestacao != 0:
            if atraso == 0:
                cobrado = prestacao
                print ("\nValor pago na %iª prestação: R$ %.2f.\n" %(parcela, cobrado))
                break
            
            else:
                cobrado = prestacao + (prestacao * ((3 + atraso * 0.1) / 100))
                print ("\nValor pago na %iª prestação: R$ %.2f.\n" %(parcela, cobrado))
                break
                

        else:
            print ("\nValor Total das Prestações: R$ %.2f." %total)
            print ("Quantidade de Prestações: %i." %parcela)
            break
    return cobrado

while x == 0:
    parcela += 1
    total = total + y

    while True:
        try:
            valor = float (input ("Digite o valor da prestação: "))
            break
        except ValueError:
            print ("\nEntrada Inválida! Utilize apenas números. Por favor!\n")

    if valor != 0:
        while True:
            try:
                dias = int (input ("Digite a quantidade de dias de atraso: "))
                y = valorPagamento (valor, dias)
                break
            except ValueError:
                print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

    else:
        valorPagamento (0, 0)
        x = 1
        break
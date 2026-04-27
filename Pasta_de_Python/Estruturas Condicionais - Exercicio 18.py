numero = int (input ("Digite um número inteiro maior que 0: "))

if numero <= 0:
    print ("Número Inválido.")
else:
    soma = sum(int(digito) for digito in str(numero))
    print (soma)
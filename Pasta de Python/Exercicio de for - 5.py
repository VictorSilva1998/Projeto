lista = []
n = int (input ("Quantos números há no conjunto: "))

for x in range (n):
    y = int (input ("Digite um número do conjunto: "))
    lista.append (y)

print ("Menor valor no conjunto: ", min (lista))
print ("Maior valor no conjunto: ", max (lista))
print ("Soma dos valores no conjunto: ", sum (lista))

a = sum (lista)

print ("Média dos valores no conjunto: ", a / n)
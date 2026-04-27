print ("M - Matutino")
print ("V - Vespertino")
print ("N - Noturno")

x = input ("Com base nos exemplos acima, digite o turno que você estuda: ")

if x=="M":
    print ("Bom dia!")
elif x=="V":
    print ("Boa tarde!")
elif x=="N":
    print ("Boa noite!")
else:
    print ("Valor Inválido!")
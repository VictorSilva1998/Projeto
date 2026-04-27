sexo = input ("Digite M para Mulher e H para Homem: ")
altura = float (input ("Digite a sua altura: "))

homens = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

if sexo == "M":
    print ("Peso ideal: %.2f." %mulheres)
elif sexo == "H":
    print ("Peso ideal: %.2f." %homens)
else:
    print ("Opção Invalida.")
print ("MG - Mato Grosso")
print ("SP - São Paulo")
print ("RJ - Rio de Janeiro")
print ("MS - Mato Grosso do Sul")

estado = input ("Digite a abreviação do estado desejado: ")

if estado == "MG":
    produto = float (input ("Digite o valor do produto: "))
    resultado = produto * 1.07
    print ("O valor do produto será de %.2f." %resultado)
elif estado == "SP":
    produto = float (input ("Digite o valor do produto: "))
    resultado = produto * 1.12
    print ("O valor do produto será de %.2f." %resultado)
elif estado == "RJ":
    produto = float (input ("Digite o valor do produto: "))
    resultado = produto * 1.15
    print ("O valor do produto será de %.2f." %resultado)
elif estado == "MS":
    produto = float (input ("Digite o valor do produto: "))
    resultado = produto * 1.08
    print ("O valor do produto será de %.2f." %resultado)
else:
    print ("Estado digitado incorreto.")
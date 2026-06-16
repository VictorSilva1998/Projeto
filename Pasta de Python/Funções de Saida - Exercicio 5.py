def inverter(numero):
    texto = str(numero)
    texto_invertido = texto[::-1]
    return int(texto_invertido)

invertido = int (input ("Digite um número para inverter: "))

resultado = inverter (invertido)
print (resultado)
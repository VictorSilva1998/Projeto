distancia = float (input ("Digite a distância em Km percorrida pelo carro: "))
gasolina = float (input ("Digite a quantidade em Litros de gasolina consumida: "))

consumo = distancia / gasolina

if consumo < 8:
    print ("Venda o carro!")
elif consumo >= 8 and consumo <= 14:
    print ("Econômico!")
elif consumo > 14:
    print ("Super Econômico!")
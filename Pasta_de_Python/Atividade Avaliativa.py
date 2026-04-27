print ("-- Resevartório de Água --")

altura = float (input ("Digite a altura (cm): "))
largura = float (input ("Digite a largura (cm): "))
comprimento= float (input ("Digite o comprimento (cm): "))
c_diario = float (input ("Digite o valor do consumo médio diário (litros/dia): "))

cap_total = (altura*largura*comprimento)/1000
auton_reser = cap_total / c_diario

print ("Capacidade do Reservatório= %.2f litros " %cap_total)
print("Autonomia do Reservatório= %.2f dias" %auton_reser) 
print ("Agora, vamos classificar o consumo")

if auton_reser < 2:
    print ("\nConsumo Elevado")
elif auton_reser >= 2 and auton_reser < 7:
    print("\nConsumo Moderado")
elif(auton_reser > 7):
    print("\nConsumo Baixo")
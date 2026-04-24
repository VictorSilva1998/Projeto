x = float (input ("Digite um número: "))
y = float (input ("Digite outro número: "))

if x > y:
    resultado = x - y
    print ("O número %.2f e o maior com diferença de %.2f do outro." %(x,resultado))
elif y > x:
    resultado = y - x
    print ("O número %.2f e o maior com diferença de %.2f do outro." %(y,resultado))
elif x == y:
    print ("Os dois números são iguais.")
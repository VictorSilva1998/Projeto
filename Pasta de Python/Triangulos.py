x = float (input ("Digite o valor do primeiro lado do triângulo: "))
y = float (input ("Digite o valor do segundo lado do triângulo: "))
z = float (input ("Digite o valor do terceiro lado do triângulo: "))

if x==y and y==z:
    print ("Triângulo Equilátero")
elif x==y or x==z or y==z:
    print ("Triângulo Isósceles")
else:
    print ("Triângulo Escaleno")
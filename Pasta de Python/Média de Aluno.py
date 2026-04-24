n1 = float (input ("Digite a primeira nota do aluno: "))
n2 = float (input ("Digite a segunda nota do aluno: "))

media = (n1+n2)/2

if media >= 7 and media < 10:
    print ("Aprovado")
elif media < 7:
    print ("Reprovado")
elif media ==  10:
    print ("Aprovado com Distinção")
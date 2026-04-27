n1 = int (input ("Digite a primeira nota do aluno: "))
n2 = int (input ("Digite a segunda nota do aluno: "))
n3 = int (input ("Digite a terceira nota do aluno: "))

media = (n1 + n2 + n3 * 2) / 4

if media >= 60:
    print ("Aprovado")
else:
    print ("Reprovado")
n1 = float (input ("Digite a nota do Trabalho de Laboratório do aluno: "))
n2 = float (input ("Digite a nota da Avaliação Semestral do aluno: "))
n3 = float (input ("Digite a nota do Exame final do aluno: "))

media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

if media >= 0 and media <= 2.9:
    print ("Reprovado")
elif media >= 3 and media <= 5.9:
    print ("Recuperação")
elif media >= 6 and media <= 10:
    print ("Aprovado")
else:
    print ("Valores Inválidos")
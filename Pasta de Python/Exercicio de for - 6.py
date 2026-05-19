lista = []
n = int (input ("Quantas pessoas há na turma: "))

for x in range (n):
    y = int (input ("Digite a idade de um dos alunos: "))
    lista.append (y)

a = sum (lista)
media = a / n

if media >= 0 and media <= 25:
    print ("\nA turma é jovem!")

elif media >= 26 and media <= 60:
    print ("\nA turma é adulta!")

else:
    print ("\nA turma é idosa!")
nome = input ("Digite o nome do aluno: ")
idade = int (input ("Digite a idade do aluno: "))
sexo = input ("Digite o sexo do aluno: ")
nota1 = float (input ("Digite a primeira nota do aluno: "))
nota2 = float (input ("Digite a segunda nota do aluno: "))

media = (nota1+nota2)/2

print ("\nAluno: %s" %nome)
print ("Idade: %i" %idade)
print ("Sexo: %s" %sexo)
print ("Primeira nota: %.2f" %nota1)
print ("Segunda nota: %.2f" %nota2)
print ("Média: %.2f" %media)
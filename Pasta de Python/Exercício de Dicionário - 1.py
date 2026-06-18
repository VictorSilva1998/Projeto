alunos = {"Alanys": 18, "João": 20, "Adalberto": 16, "Vinicius": 17, "Lucas": 20}

estudante = input ("Digite o nome do aluno desejado: ")
if estudante in alunos:
    print(f"O aluno(a) {estudante} tem {alunos [estudante]} anos de idade.")
else:
    print(f"O/A {estudante} não está na turma.")
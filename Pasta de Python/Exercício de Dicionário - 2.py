semana = {"segunda": "Português", "terça": "Matemática", "quarta": "Inglês", "quinta": "Geografia", "sexta": "História", "sábado": "nenhuma", "domingo": "nenhuma"}

dia = input ("Digite o dia da semana desejado: ")
if dia in semana:
    print (f"{dia} sua aula é: {semana [dia]}.")
else:
    print (f"{dia} não encontrado.")
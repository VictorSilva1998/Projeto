mes = int (input ("Digite um número entre 1 e 12: "))

ano = [0,"Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

if mes >= 1 and mes <= 12:
    print (ano [mes])
else:
    print ("Número Inválido")
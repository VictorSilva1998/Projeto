dia = int (input ("Digite um número entre 1 e 7: "))

semana = [0,"Domingo","Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado"]

if dia >= 1 and dia <= 7:
    print (semana [dia])
else:
    print ("Número Inválido")
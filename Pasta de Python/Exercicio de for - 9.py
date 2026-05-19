y = int (input ("Quantas cidades brasileiras deseja informar: "))

codigo = []
cidade = []
estado = []
passeio = []
vitimas = []
sem = []
bebado = []
total = []

for x in range (1, y + 1):

    a = str (input ("\nInforme o código da %i° cidade: " %x))
    b = str (input ("Informe o nome da %i° cidade: " %x))
    c = str (input ("Informe o nome do estado da %i° cidade: " %x))
    d = int (input ("Informe o número de veiculos de passeio da %i° cidade: " %x))
    e = int (input ("Informe o número de acidentes de trânsito com vítimas na %i° cidade: " %x))
    f = int (input ("Informe o número de acidentes de trânsito sem vítimas na %i° cidade: " %x))
    g = int (input ("Informe o número de acidentes com motoristas embriagados na %i° cidade: " %x))

    total_acidentes = e + f

    codigo.append (a)
    cidade.append (b)
    estado.append (c)
    passeio.append (d)
    vitimas.append (e)
    sem.append (f)
    bebado.append (g)
    total.append (total_acidentes)

max_total = max (total)
min_total = min (total)
maior_acidentes = total.index (max_total)
menor_acidentes = total.index (min_total)
nome_max = cidade [maior_acidentes]
nome_min = cidade [menor_acidentes]
media_veiculos = (sum (passeio)) / y
max_veiculos = max (passeio)
min_veiculos = min (passeio)
maior_veiculos = passeio.index (max_veiculos)
menor_veiculos = passeio.index (min_veiculos)
cidade_veiculos_maior = cidade [maior_acidentes]
cidade_veiculos_menor = cidade [menor_acidentes]
menos_de_2000 = [num for num in passeio if num < 2000]
acidentes_2000 = (sum (menos_de_2000)) / (len (menos_de_2000))

print ("\nResumo:\n")
print ("O maior índice de acidentes de trânsito é %i na cidade %s." %(max (total), nome_max))
print ("O menor índice de acidentes de trânsito é %i na cidade %s." %(min (total), nome_min))
print ("A média de veículos de todas as cidades juntas é de %.2f." %media_veiculos)
print ("A total de veículos de todas as cidades juntas é de %i." %sum(passeio))
print ("A cidade com o maior número de veículos é %s." %cidade_veiculos_maior)
print ("A cidade com o menor número de veículos é %s." %cidade_veiculos_menor)
print ("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de %.2f." %acidentes_2000)
print ("O número total de acidentes de trânsito é de %i, sendo %i com vitimas e %i sem vitimas." %(sum (total), sum (vitimas), sum (sem)))
print ("Dos acidentes de trânsito com vítimas, o condutor estava embriagado em %i." %sum (bebado))
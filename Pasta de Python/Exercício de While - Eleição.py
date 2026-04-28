escolha = 1
joao = 0
adalberto = 0
vinicius = 0
daniel = 0
nulo = 0
branco = 0

while escolha != "0":
    print ("========= Urna Eletrônica =========")
    print ("1 - João")
    print ("2 - Adalberto")
    print ("3 - Vinicius")
    print ("4 - Daniel")
    print ("5 - Voto Nulo")
    print ("6 - Voto em Branco")
    print ("0 - Resultados e sair")
    escolha = str (input ("Escolha uma das opções acima: "))

    if escolha == "1":
        joao = joao + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "2":
        adalberto = adalberto + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "3":
        vinicius = vinicius + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "4":
        daniel = daniel + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "5":
        nulo = nulo + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "6":
        branco = branco + 1
        print ("\nVoto Aceito!\n")
    elif escolha == "0":
        total = joao + adalberto + vinicius + daniel + nulo + branco
        candidatos = [joao, adalberto, vinicius, daniel]
        nomes = ["João", "Adalberto", "Vinicius", "Daniel"]
        x = candidatos.index (max (candidatos))

        print ("\nJoão = %i" %joao)
        print ("Adalberto = %i" %adalberto)
        print ("Vinicius = %i" %vinicius)
        print ("Daniel = %i" %daniel)
        print ("Votos Nulos = %i" %nulo)
        print ("Votos em Branco = %i" %branco)
        print ("Total de votos = %i" %total)
        print ("Ganhador = ", nomes [x])
    else:
        print ("\nOpção Inválida!\n")
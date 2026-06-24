import os

nome_pasta = input ("Digite o nome da pasta: ")

if not os.path.exists(nome_pasta):
    nome_arquivo = input ("Digite o nome do arquivo: ")

    nome_arquivo += ".txt"

    os.mkdir (nome_pasta)
    os.chdir (nome_pasta)

    with open (nome_arquivo, "w") as f:
        f.write ("Tudo certo nada resolvido")

else:
    print(f"A pasta '{nome_pasta}' já existe.")
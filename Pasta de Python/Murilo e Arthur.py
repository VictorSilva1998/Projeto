import pandas as pd

dados = {"Nomes": ["Ana", "Bruno", "Carlos", "Diana"], "Nota 1": [8, 5.5, 9, 4], "Nota 2": [7, 6, 8.5, 6]}

tabela = pd.DataFrame (dados)
print (tabela)

media = tabela ["Idade"].mean()
print (f"\nIdade Média é: {media}.")
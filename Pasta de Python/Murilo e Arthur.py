import pandas as pd

dados = {"Nomes": ["Ana", "Bruno", "Carlos", "Diana"], "Nota 1": [8, 5.5, 9, 4], "Nota 2": [7, 6, 8.5, 6]}

tabela = pd.DataFrame (dados)

media = ["Nota 1", "Nota 2"]
tabela['Média'] = tabela[media].mean(axis=1)

print (tabela)
traducao = {"hello": "olá", "goodbye": "adeus", "thank you": "obrigado"}

palavra_ingles = input("Digite uma palavra em inglês: ")
if palavra_ingles in traducao:
    print(f"A tradução de {palavra_ingles} é {traducao[palavra_ingles]}.")
else:
    print("Essa palavra não está no dicionário de tradução.")
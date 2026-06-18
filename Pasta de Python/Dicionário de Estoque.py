estoque = {"camisetas": 50, "tênis": 25, "bonés": 100}

produto = input("Digite o produto desejado: ")
if produto in estoque:
    print(f"{produto} está em estoque com {estoque[produto]} unidades disponíveis.")
else:
    print(f"{produto} não está disponível em estoque.")
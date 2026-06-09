def cadastro():
    name = input ("Qual seu nome: ")
    age = int (input ("Idade: "))
    return name, age

print ("Iniciando cadastro...")
nome, idade = cadastro ()
print ("Cadastro realizado com sucesso!")
print ("Seu nome é", nome,"e voce tem", idade,"anos de idade.")
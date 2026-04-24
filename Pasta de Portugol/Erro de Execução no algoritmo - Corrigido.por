programa {
  funcao inicio() 
  {
real nota1,nota2,nota3,nota4,media,total
cadeia nome,sexo,endereco,telefone,cidade,estado,pais,pai,mae
inteiro idade,filhos

escreva ("\nDigite o seu nome = ")
leia (nome)
escreva ("\nDigite o seu sexo = ")
leia (sexo)
escreva ("\nDigite o seu Endereço = ")
leia (endereco)
escreva ("\nDigite o seu Telefone = ")
leia (telefone)
escreva ("\nDigite o sua Cidade = ")
leia (cidade)
escreva ("\nDigite o seu Estado = ")
leia (estado)
escreva ("\nDigite o seu País = ")
leia (pais)
escreva ("\nDigite o nome do seu Pai = ")
leia (pai)
escreva ("\nDigite o nome da sua Mãe = ")
leia (mae)
escreva ("\nDigite a sua Idade = ")
leia (idade)
escreva ("\nDigite o numero de filhos = ")
leia (filhos)
escreva ("\nDigite a nota 1 = ")
leia (nota1)
escreva ("\nDigite a nota 2 = ")
leia (nota2)
escreva ("\nDigite a nota 3 = ")
leia (nota3)
escreva ("\nDigite a nota 4 = ")
leia (nota4)
total=(nota1+nota2+nota3+nota4)/4
escreva(" Olá Sr ",nome, ", idade ",idade,", telefone ",telefone,", situado no endereço ",endereco, ", " ,cidade, ", ",estado, ", ",pais, ", filho de ",pai, " e ",mae, " atualmente com ",filhos, " filhos\n")
escreva(" Possui média  = ",total)
  }
}

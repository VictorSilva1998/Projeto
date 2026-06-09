def soma (x, y):
    result = x + y
    return result

a = int (input ("Primeiro número: "))
b = int (input ("Segundo número: "))

res = soma (a, b)
print ("Soma:", res)

def inverte (nome, sobrenome):
    nomeInverso = sobrenome+","+nome
    return nomeInverso

nome = input ("Nome: ")
sobrenome = input ("Sobrenome: ")
invertido = inverte (nome, sobrenome)
print ("Olá", invertido)
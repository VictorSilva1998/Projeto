def soma (x, y, z):
    result = x + y + z
    return result

while True:
    try:
        a = int (input ("Primeiro número: "))
        break
    except ValueError:
        print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

while True:
    try:
        b = int (input ("\nSegundo número: "))
        break
    except ValueError:
        print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")
while True:
    try:
        c = int (input ("\nTerceiro número: "))
        break
    except ValueError:
        print ("\nEntrada Inválida! Utilize apenas números inteiros. Por favor!\n")

res = soma (a, b, c)
print ("\nSoma:", res)
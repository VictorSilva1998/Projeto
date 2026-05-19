n = int (input ("Digite o número do termo da série de Fibonacci desejado: "))
x, y = 0 ,1

fibonacci = []

for a in range (n):
    fibonacci.append (str(x))
    x, y = y, x + y

print (" ".join (fibonacci))
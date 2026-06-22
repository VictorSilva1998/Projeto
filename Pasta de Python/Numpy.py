import numpy as np

valores = np.array([15, 22, 35, 48, 55])

print("Média:", np.mean(valores))        # Média dos valores
print("Soma:", np.sum(valores))          # Soma de todos os elementos
print("Maior valor:", np.max(valores))   # Valor máximo
print("Menor valor:", np.min(valores))   # Valor minimo

dados = np.array([10, 20, 30, 40])

# Multiplicar todos os valores por 2
resultado = dados * 2
print(resultado)  # Saída: [20 40 60 80]

# Somar 5 a todos os elementos
print(dados + 5)  # Saída: [15 25 35 45]

# Array unidimensional (vetor) a partir de uma lista
vetor = np.array([1, 2, 3, 4, 5])

# Matriz bidimensional 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Criar uma matriz de zeros ou uns automaticamente
zeros = np.zeros((3, 3)) # Matriz 3x3 de zeros
uns = np.ones((2, 2))    # Matriz 2x2 de uns
arange = np.arange(1,10,2)

print(vetor)
print(matriz)
print(zeros)
print(uns)
print (arange)
import copy

lista_original = [[1, 2], [3, 4]]
lista_profunda = copy.deepcopy(lista_original)

# Modificando a lista aninhada não afeta a original
lista_profunda[1][0] = 99
print(lista_original)  # Saída: [[1, 2], [3, 4]]
print(lista_profunda)
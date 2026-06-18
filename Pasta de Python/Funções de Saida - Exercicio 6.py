import random

def embaralhar(texto):
    string = list(texto)
    random.shuffle(string)
    resultado = []
    
    for char in string:
        decisao = random.randint(0, 1)

        if decisao == 0:
            resultado.append(char.upper())
        else:
            resultado.append(char.lower())
            
    return ''.join(resultado)

teste = str (input ("Digite uma string para ser embaralhada: "))
string_modificado = embaralhar(teste)
print("\nString Embaralhada: ", string_modificado)
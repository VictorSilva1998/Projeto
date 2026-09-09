from operacao import Operacao

class Divisao (Operacao):
    simbolo = "/"
    nome = "Divisão"

    def calcular(self):
        if self.b == 0:
            raise ZeroDivisionError
        return self.a / self.b
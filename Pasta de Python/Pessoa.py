class Pessoa:
    def __init__(self, altura, nome): 
        self.altura = altura
        self.nome = nome

    def andar(self, passos):
        print ("Estou andando", passos, "passos")

    def respirar(self, respiradas):
        print ("Estou respirando", respiradas, "ares por segundo")

    def somar(self, valor1, valor2):
        resultado = valor1 + valor2
        print (resultado)

    def subtrair(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado

p1 = Pessoa(1.95, "Victor")
p2 = Pessoa(1.75, "Vinicius")

print (p1.altura)
print (p1.nome)
p1.andar (200)
p1.respirar (50)
p1.somar (10, 20)
print (p1.subtrair (10, 20))

print (p2.altura)
print (p2.nome)
p2.andar (100)
p2.respirar (1000)
p2.somar (30, 50)
print (p2.subtrair (30, 50))
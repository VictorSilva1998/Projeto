tradutor = {}
tradutor ["pineapple"] = "abacaxi"
tradutor ["apple"] = "maçã"
tradutor ["orange"] = "laranja"

print (type (tradutor))
print (tradutor)

tradutor1 = {}
tradutor1 = {"pineapple": "abacaxi", "apple": "maçã", "orange": "laranja"}

print (type (tradutor1))
print (tradutor1)

print (tradutor1 ["apple"])

print (tradutor1)
del (tradutor1 ["apple"])
print (tradutor1)

print (tradutor1.pop ("banana", "Fruta não encontrado"))
print (tradutor1.pop ("orange", "Fruta não encontrado"))

tradutor1.clear ()
print (tradutor1)

tradutor1 = {}
tradutor1 = {"pineapple": "abacaxi", "apple": "maçã", "orange": "laranja"}
print ("pineapple" in tradutor1)

print ("laranja" in tradutor1.values ())
print (tradutor1.values ())

tradutor1 = {}
tradutor1 = {"pineapple": "abacaxi", "apple": "maçã", "orange": "laranja"}
print (tradutor1)
tradutor1 ["apple"] = "goiaba"
print (tradutor1)

dados = {"Crossfox": {"km": 35000, "ano": 2005}, "DS5": {"km": 17000, "ano": 2015}, "Fusca": {"km": 130000, "ano": 1979}, "Jetta": {"km": 56000, "ano": 2011}, "Passat": {"km": 62000, "ano": 1999}}
print (dados ["Fusca"]["ano"])

mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print (mydict.keys ())

aluno = {"nome": "Maria", "idade": 20, "curso": "ADS"}
print (aluno.items)
for chave, valor in aluno.items ():
    print (chave, "->", valor)
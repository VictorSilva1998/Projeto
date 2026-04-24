lista = ["Victor",64,23,87,"Maçã","Pera"]
lista1 = [1,2,3,4,5]
uma_lista = ["a","b","e","f","g","h"]
a = [28,22,26,21]
b = [22,23,22,24,22,25,22]

print (len (lista))
print (lista [2])
print (lista [0][3])
print ("Maçã" in lista)
print ([1,2] + [3,4])
print (lista + [6,7,8,9])
print (["Teste"] * 4)
print ([1,2, ["Olá","Adeus"]] * 2)

print (lista + lista1)

print (min (lista1))
print (max (lista1))
print (sum (lista1))

print (uma_lista [1:3])
print (uma_lista [:4])
print (uma_lista [3:])
print (uma_lista [:])
print (uma_lista [0:6])

lista [0] = "Pera"
lista [-1] = "Victor"
lista [1:3] = [75,48]
print (lista)

uma_lista [2:2] = ["c","d"]
print (uma_lista)

del uma_lista [1]
del lista [1:4]
print (uma_lista)
print (lista)

a.append (4)
print (a)

a.sort ()
lista1.sort (reverse=True)
print (a)
print (lista1)

print (a.index (26))

a.insert (1,100)
print (a)

print (b.count (22))
b.pop ()
print (b)
b.pop (2)
print (b)

a.extend ([29,30])
print (a)
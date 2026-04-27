a = "victor"
b = "VICTOR"
c = "12345"
d = "Victor Alexandre"
e = "Victor-Alexandre-da-Silva"

print (len (a))
print (a.capitalize())
print (a.upper())
print(b.lower())
print (b.islower())
print (b.casefold())
print (c.isdigit())
print (d.replace ("Alexandre","Silva"))
print (e.split ("-"))
print (d.find ("Alexandre"))
print ("Alexandre" in d)
print (d.count ("r"))
print (e [5])
print (e [:6])
print (e [-5:])
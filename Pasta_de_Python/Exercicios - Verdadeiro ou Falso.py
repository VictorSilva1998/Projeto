a=1
b=2

print ("A)", a!=2 or b==1)
print ("B)", a!=1 or b==1)
print ("C)", not (a==1))
print ("D)", a==2 and b!=1)

x=10
y=15
z=25

print (x == z - y and z != y - x or not y != z - x)
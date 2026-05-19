x = int (input ("Digite o valor de x: "))
y = int (input ("Digite o valor de y: "))

if x < y:
    for n in range (x+1,y):
        print (n)

else:
    for n in range (y+1,x):
        print (n)
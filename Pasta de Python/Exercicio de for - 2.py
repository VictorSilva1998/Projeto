x = 0
x = int (input ("Digite o valor de x: "))
y = int (input ("Digite o valor de y: "))

if x < y:
    for n in range (x+1,y):
        x = x + y
    print (x)

else:
    for n in range (y+1,x):
        y = y + x
    print (y)
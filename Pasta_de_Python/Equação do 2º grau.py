a = int (input ("Digite o valor de a: "))

if a != 0:
    b = int (input ("Digite o valor de b: "))
    c = int (input ("Digite o valor de c: "))

    delta = b**2-4*a*c
    x1 = (-b+delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a

    if delta < 0:
        print ("A equação não possui raizes reais.")
    elif delta == 0:
        x = (-b+delta**0.5)/2*a
        print ("A equação possui apenas uma raiz real. X = %.2f" %x)
    elif delta > 0:
        print ("A equação possui duas raizes reais. X1 = %.2f e X2 = %.2f" %(x1,x2))
else:
    print ("A equação não é de segundo grau.")
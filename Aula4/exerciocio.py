a = int (input ("Lado a: ") )
b = int (input ("Lado b: ") )
c = int (input ("Lado c: ") )
if (a < b + c) and (b < a + c) and (c < a + b) :
    if (a == b) and (b == c): 
        print("triangulo equilatero")
    else:
        if (a == b) or (a == c) or (b == c):
            print("triangulo isosceles")
        else:
            print("triangulo escaleno")
else:
    print("n tem triangulo")            
a,b,c = input("Length 1: "), input("Length 2: "), input("Length 3: ")

if a+b < c or a+c < b or b+c < a:
    print("Not a triangle")
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
    print("Is isosceles")
else:
    print("Is not isosceles")

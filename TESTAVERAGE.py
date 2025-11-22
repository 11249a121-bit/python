a = int(input("Enter the marks"))
b = int(input("Enter the marks"))
c = int(input("Enter the marks"))
x = (a+b)/2
y = (b+c)/2
z = (a+c)/2
if x>y and x>z:
    print("average of a and b is best",x)
elif y>z and y>x:
    print("average of b and c is best",y)
elif z>x and z>y:
    print("average of a anc c is best",z)    


import cmath
a=int(input("enter the no "))
b=int(input("enter the no "))
c=int(input("enter the no "))
z=b*b-4*a*c
z1=cmath.sqrt(z)
x1=(-b+z1)/2*a
x2=(-b-z1)/2*a
print("solution1 =",x1,"\n solution2 =",x2)

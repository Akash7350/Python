import math
n1=int(input("Enter a number1: "))
n2=int(input("Enter a number2: "))
a=n1
b=n2
print("gcd:",math.gcd(n1,n2))
#print("lcm",math.lcm(n1,n2))
lcm=(n1*n2)/math.gcd(n1,n2)


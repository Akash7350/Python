def gcd(n1,n2):
	if n1==n2:
		return n1
	if n1>n2:
		return gcd(n1-n2,n2)
	else:
		return gcd(n1,n2-n1)
#driver cide
n1=int(input("enter the first number"))
n2=int(input("enter the secodn number"))
print("gcd of given number is : ",gcd(n1,n2))				

def sumdigit(n):
	if n==0:
		return 0
	return (n%10+sumdigit(n//10))
#drivercode
n=int(input("enter n"))
print("sum of digit = ",sumdigit(n))		

#n=int(input("enter times of print"))

def hello(n):
	if(n!=0):
		print("hello")
		hello(n-1)
n=int(input("enter the number"))
hello(n)		

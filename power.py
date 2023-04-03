def power(x,y):
	if(y==0):
		return 1
	return x*(power(x,y-1))
#driver oced
x=int(input("enter the x value"))
y=int(input("enter the y value"))
print("x to the power of y is: ",power(x,y))		
	
	

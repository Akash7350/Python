#reversed() reversed is a function or method which takes sequence object as a input and generate a list of elements of that object in reversed order for example s1="python"
#reversed(s1)

n=int(input('Enter the number :'))
n1=n
s1=""
while n!=0:
    rem=n%2
    s1=s1+str(rem)
    n=n//2
result="".join(reversed(s1))
print("binary :",result)

n=n1
s1=""
while n!=0:
    rem=n%8
    s1=s1+str(rem)
    n=n//8
result="".join(reversed(s1))
print("octal:",result)

n=n1
dict={10:"A",11:'B',12:'C',13:'D',14:'E',15:'F'}
s1=""
while n!=0:
	rem=n%16
	n=n//16
	if rem<10:
		s1=s1+str(rem)
	else:
		s1=s1+dict[rem]
		result="".join(reversed(s1))
print("hexa: ",result)









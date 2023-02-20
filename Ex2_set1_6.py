n=int(input('Enter the number: '))
n1=n
rev=0
while n!=0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
if rev==n1:
        print("Palindrome")
else:
	print("not Palindrome")

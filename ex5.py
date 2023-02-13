n=input("Enter the Number")
cnt=len(n)
no=int(n)
n=no
sum=0
while no!=0:
    rem=no%10
    no=no//10
    sum=sum+rem**cnt
if(n==sum):
    print("Armstrong")
else:
    print("Not Armstrong")

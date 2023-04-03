n=int(input("enter the number"))
n1=n
str1=""
while n!=0:
    rem=n%2
    n=n//2
    str1=str1+str(rem)
print(str1)
#for i in range(len(str1)-1,-1,-1):
#    print(str1[i])
#str1=str1[::-1]
str1="".join(reversed(str1)) 
print("binary",str1)

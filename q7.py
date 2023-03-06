#reversed is a function/method which takes sequence object input and generate a list of elements of that object in reverse order for e.g 
n=int(input("Enter the number: "))
n1=n
s1=""
while n!=0:
    rem=n%2
    s1=s1+str(rem)
    n=n//2
    res="".join(reversed(s1))
print("Binary:", res)

n=int(input("Enter the number: "))
n1=n
s1=""
n=n1
while n!=0:
    rem1=n%8
    s1=s1+str(rem1)
    n=n//8
    res1="".join(reversed(s1))
print("Octal: ",res1)    

n=int(input("Enter the number: "))
n1=n
dict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
s1=""
n=n1
while n!=0:
    rem=n%16
    n=n//16
    if rem<10:
        s1=s1+str(rem)
    else:
        s1=s1+dict[rem]
        
    res="".join(reversed(s1))
print("Hex: ",res)

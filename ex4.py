n=int(input("Enter the Number"))
if (n==2 or n==3):
    print("Is prime")
elif(n%2==0):
    print("Not prime")
else:
      for i in range(3,n,2):
          if (n%i==0):
                print("Number is prime")
                break
      if(i==n-2):
                print("Prime")

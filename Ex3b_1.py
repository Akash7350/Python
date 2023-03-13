#Create a tuple program
t1=()
#Empty Tuple
t2=("Akash Rathod",19,56.6,True)

#tuple with different data type
print(t2)

#tuple with numbers and print one item
t3=(2,3,4,6,7)

#to print each item
for i in t3:
    print(i)

#unpack the Tuple
n1,n2,n3,n4,n5=t3
print("Addition of tuple elements :",n1+n2+n3+n4+n5)

#add item in tuple
l1=list(t3) #convert tuple in list
l1.append(100)#add 100

t3=tuple(l1)#convert list to tuple
print(t3)

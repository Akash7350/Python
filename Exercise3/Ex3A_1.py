n=int(input('Enter Number of list elements :'))
l1=[]
print("Enter the list Elements :")
for i in range(1,n+1):
    l1.append(int(input()))
print("list is ",l1)

#Sum of list element
sum=0
for i in l1:
   sum+=i
print("Sum is : ",sum)

#Multiplication of list elements
prod=1
for i in l1:
   prod=prod*i
print("Multplication is :",prod)
#smallest elements of list
print("Smallest Element is :",min(l1))

#Largest Element of list 
print("Largest Element is =",max(l1))

#Second Largest/Smallest number form a list
l1.sort()
print("Second Smallest is:",l1[1])
print("Second Largest is:",l1[-2])
#Counting the element
print("count is :",len(l1))

#Removing 
l1=list(set(l1))
print("List without Duplicate :",l1)

#Descinding sort
l1.sort(reverse=True)
print("Descinding order: ",l1)

#check a list is empty or not
l2=[2, 4]
if l2:
    print("List is not empty")
else:
    print("List Empty")

#8.clone or copy
l2=l1.copy()
print("Copied list is :",l2)

#Union, intersection and difference of two lists
l3=[2,3,5,8,7]
l4=[2,3,90,7,11]
print("Union :",list(set(l3+l4)))

#10.intersection and difference of two lists
print("intersection :",list(set(l3).intersection(set(l4)) ))

#difference between 2
print("Difference :",list(set(l3)-set(l4)))



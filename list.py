n = int(input("enter number of list elements"))
l1=[]
print("Enter list elements")
for i in range(1,n+1):
	l1.append(int(input()))
print("List is :",l1)	
#sum of list elements
sum=0
for i in l1:
	sum=sum+i
print("sum is :", sum)	
#multiplication of list elements
product=1
for i in l1:
	product=product*i
print("produst is:",product)	
#smlallset element of list
print("smallest element =", min(l1))
#largest elemnt of list
print("largest element =", max(l1))
#second samallest second largest
l1.sort()
print("second smallest =",l1[1])
print("second largest =",l1[-2])
#counting no of elemnts
print("count = ", len(l1))
#removing duplicate
l1= list(set(l1))
print("list without duplicates",l1)
#resverse descending sort
l1.sort(reverse=True)
print("descending order = ",l1)
#list is empty or not
l2=[]
if l2:
	print("list is not empty")
else:
	print("list is empty")	
#clone/copy a list
l2=l1.copy()
print("copiesd list is", l2)
#union diff inter
l3=[2,3,4,6,7]
l4=[3,5,8,2,9]
print("union is: ", list(set(l3+l4)))
#intersection of 2 list
print("intersection is:", list(set(l3).intersection(set(l4))))


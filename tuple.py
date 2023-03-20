import copy
#create a tuple
t1=()#empty tuple
t2=("jatin",20, 72.5, True)#tuple with diffrent data types
print(t2)
t3=(2,4,5,3,2)
#print each item
for i in t3:
	print(i)
#unpack the tuple
l1,l2,l3,l4,l5=t3
print("addition of tuple elements : ",l1+l2+l3+l4+l5)
#add item in tuple
l1=list(t3)#convert tuple to list
l1.append(100)#add hundered
t3=tuple(l1)#convert in tuple 
print(t3)
#tuple to string
t4=('j','a','t','i','n')
s1=''.join(t4)
print(s1)
#get 4th element and last 4th element	
print("4th elemnt",t4[3])
print("4th elemnt from last",t4[-4])
# create a clone of a tuple
t5=copy.deepcopy(t4)
t4=t4+("hello",5)
print("original copy",t4)
print("clone tuple =",t5)
#to find the repeated items of the tuple
l1=[]
t6=(3,4,5,3,4,2,6,7,8)
for i in t6:
	if t6.count(i)>1:#no of occurances by count
		if i not in l1:
			print(i)
			l1.append(i)
#exist in tuple	
num=int(input("Enter number to search :"))
if num in t6:
	print("present")
else:
	print("not present")
#covert list to tuple
l1=[3,4,5]
print("list to tuple : ",tuple(l1))	
#remove elements to tuple	
l2=list(t6)
print(t6)
num=int(input("enter number to delete"))
l2.remove(num)
t6=tuple(l2)
print("tuple after delete = ",t6)

	












		
		

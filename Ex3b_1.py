import copy


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
l1.append(100)#add 100:wq


t3=tuple(l1)#convert list to tuple
print(t3)

t4=("A", 'k','a','s','h')
s1=''.join(t4)
print(s1)

#b)7get 4th element and last 4th element of a tuple
print('4th element=',t4[3])
print('4rth elements from last=',t4[-4])

#b)8.to create the colon of a tuple

t5=copy.deepcopy(t4)
t6=("Hello",)
t4=t4+t6
print("original copy",t4)
print('clone copy tuple =',t5)

#find the repeated 
t7=('10','22','30','40',"50","10",'5','5')
for i in t7:
	if t7.count(i)>1:
		if i not in l1: #(i)>1: #count occarances of 
			print(i)
			l1.append(i)
	
#to check wheter an element exists within a tuple		
num=int(input("Enter the number to search"))
if num in t7:
	print('present')
else:
	print('Not present')
	
#11. convert list to tuple
l1=['3','4','6','8']
print('list to tuple=',tuple(l1))

#remove an item from a tuple
l2=list(t7)
print(t7)
num=int(input('Enter number to delete'))
t3.remove(num)
t7=(tuple(l3))
print('Tuple after delete',t7)

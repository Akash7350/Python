#to create set
s1={}
print("Empty set=",s1)
s2={2,3,4,5,6,}
print('set of numbers =',s2)
s3={9,'Akash Rathod', 8.65,'Sycyber'}
print('Mixed data type=',s3)

#to iteration over sets
for i in s3:
	print(i)
#to add members(s) in set	
s3.add('Indira college')
print('after adding=',s3)

#to remove an item from a set if it is present in the set
s4={10,20,10,30,60,50,20}
print("s4 before the remove/delete =",s4)
s4.remove(10)
print('s4 after remove',s4)

#remove item if it from set
print("set before remove=",s4)
num=int(input('Enter number to remove='))
flag=0
for i in s4:
	if i==num:
		s4.remove(i)
		flag=1
		print("set after delete=",s4)
		break
if flag==0:
	print(num,'Is not present=')
	
#union intersection difference and symmetric difference
s5={10,20,90,40}
s6={10,20,60,40}
print('1st set =',s5)
print('2nd set =',s6)
print('union=',s5.union(s6))	

print("Intersection=",s5.intersection(s6))
print("s5-s6",s6.difference(s6))
print("s6-s5",s6.difference(s5))
print("Symmetric difference=",s5.symmetric_difference(s6))

s7={'a','b','c'}
s8={'e','f','a','b','c'}
print("s7=",s7)
print("s8=",s8)
print("is s7 subset of s8? ",s7.issubset(s8))

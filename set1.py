#create set
s1={}
print("empty set: ",s1)
s2={1,2,34,5,75,4}
print("set of numbers: ",s2)
s3={23,"Jatin Harshwal",8.73,"sy cyber"}
print("mixed datatype set: ",s3)
#itterate the set
for i in s3:
	print(i)
#add members in set
s3.add("Indira college")
print("after adding",s3)
#remove items from set
s4={10,20,10,30,60,50,20}
print("s4 before remove: ",s4)
s4.remove(10)
print("after remove: ",s4)
#remove item from set if present in set
print("set before remove",s4)
num=int(input("Enter element to remove: "))
flag=0
for i in s4:
	if i==num:
		s4.remove(num)
		flag=1
		break
print("set after delete",s4)		
if flag==0:
	print(num," is not present")		
#union intersection diffrence symdiff
s5={10,90,20,40}
s6={30,20,70,40}
print("first set: ",s5)
print("second set: ",s6)
print("union= ",s5.union(s6))
print("intersection: ",s5.intersection(s6))
print("s5-s6: ",s5.difference(s6))
print("s6-s5: ",s6.difference(s5))
print("symmetric difference: ",s5.symmetric_difference(s6))	
#subset and superset
s7={'a','b','c'}
s8={'e','f','a','b','c'}
print("s7=",s7)
print("s8=",s8)
print("is s7 subset of s8?",s7.issubset(s8))
print("is s8 superset of s7?",s8.issuperset(s7))
	
	
	
	
				

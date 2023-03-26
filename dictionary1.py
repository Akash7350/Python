#create a Dictionary
fb={'Messi':50, 'Ronaldo':100,'Neymar':30,'Pele':10}

#sort in ascending order
rs=sorted(fb.items(),key=lambda x:x[1])
print('Sorted dictionary :',rs)

#Reverse order
rs=sorted(fb.items(),key=lambda x:x[1],reverse=True)
print('Reverse order is:',rs)

#to add new item in a dictionary
fb['Akash']=20
print('Updated dictionary',fb)

#concate the dictionary
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
res={}
res.update(dic1)
res.update(dic2)
print('concatented dictionary is =',res)

#write a python script to check whether given key alredy
name=input("Enter player name to search ")
if name in fb:
	print('Player is present ')
else:
	print("Player is not present ")
	
#Search by Value
goals=int(input("Enter Goals to search :"))
for key, value in fb.items():
	if value == goals:
		print(key)
	
# iterate Using Dictionary
for i in fb.items():
	print(i)

#27 Generate and print a dictionary that contains a number
dic4={}
n=int(input('Enter a Number :'))
for i in range(1,n+1):
	dic4.update({i:i*i})
print('Genereted dictionary :',dic4)

#Generate dictionary where value is Tuple
dic5={}
for i in range (i,n+1):
	dic5.update({i:(i*i,i*i*i)})
print('tuple dictionary is :',dic5)

#Merging dictionaries
res=dict(sorted((dic1|dic2|dic3).items(),key=lambda x:x[0]))
print("Merege dictionary is ",res)

#Sum of dictionary
sum=0 
dic6={1:10,2:20,3:30,4:40}
for i in dic6:
	sum=sum+i
print("Sum =",sum)



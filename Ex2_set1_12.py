r=int(input("Enter number of rows:	"))
c=int(input("Enter number of column:	"))
m1=[]
print('Enter 1st matric:')
for i in range(r):
	a=[]
	for j in range(c): 
		a.append(int(input('Enter the Elements:	')))
	m1.append(a)
for i in range(r):
	print(m1[i])
m2=[]
print('Enter 2nd matrix:')
for i in range(r):
	a=[]
	for j in range(c):
		a.append(int(input('Enter the Elements:	')))
	m2.append(a)
for i in range(r):
	print(m2[i])
m3=[]
for i in range(r):
	a=[]
	for j in range(c):
		a.append(m1[i][j]+m2[i][j])
	m3.append(a)
print("Addition of matrix is")
for i in range(r):
	print(m3[i])				
		

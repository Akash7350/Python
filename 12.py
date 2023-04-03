r=int(input("enter no of rows"))
c=int(input("enter no of columns"))
m1=[]
print('enter first matrix')
for i in range(r):
    a=[]
    for i in range(c):
        a.append(int(input("enter the element")))
        m1.append(a)
for i in range(r):
    print(m1[i])

#addition is
r=int(input("enter no of rows"))
c=int(input("enter no of coloumns"))
m1=[]
print("enter first matrix")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("enter the element")))
    m1.append(a)
for i in range(r):
                 print(m1[i])
m2=[]
print("enter the second")
for i in range(r):
    a=[]
    for i in range(c):
        a.append(int(input("enter the element")))
    m2.append(a)
for i in range(r):
    print(m2[i])
m3=[]
for i in range(r):
    a=[]
    for j in range(c):  
        a.append(m1[i][j]+m2[i][j])
    m3.append(a)
print("addition is")
for i in range(r):    
    print(m3[i])                             



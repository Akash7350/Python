r=int(input("Enter no of rows: "))
c=int(input("Enter no of columns: "))
m1=[]
print("Enter first matrix")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("Enter Element: ")))
    m1.append(a)    
for i in range(r):
    print(m1[i])
m2=[]
print("Enter second matrix")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input("Enter Element: ")))
    m2.append(a)    
for i in range(r):
    print(m2[i])
m3=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(m1[i][j]+m2[i][j])
        m3.append(a)
print("matrix addition is")
for i in range(r):
    print(m3[i])
    

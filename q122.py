size=int(input("Enter no of columns and rows of square matrix: "))
m1=[]
print("Enter first matrix")
for i in range(size):
    a=[]
    for j in range(size):
        a.append(int(input("Enter Element: ")))
    m1.append(a)
for i in range(size):
    print(m1[i])
m2=[]
print("Enter first matrix")
for i in range(size):
    a=[]
    for j in range(size):
        a.append(int(input("Enter Element: ")))
    m2.append(a)    
for i in range(size):
    print(m2[i]) 
m3=[]
for i in range(size):
    a=[]
    for j in range(size):
        sum=0
        for k in range(size):
            sum += m1[i][k]*m2[k][j]
        a.append(sum)
    m3.append(a)
for i in range(size):
    print(m3[i])

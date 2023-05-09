'''
1. Write a python script for conversion which accepts distance in km convert to
miles, accept temperature in Celsius and convert to Fahrenheit and also accepts
time in minutes and convert it to seconds.

'''


'''
#1. conversion
a = int(input("Enter the Km to convert miles: "))
print("Km to miles is :",a * 0.621)

a = int(input("Enter Celsius to convert Fahreneit: "))
print("Fahrenit is: ", a*9/5+32)

c = int(input("Enter Number of minutes: "))
print("Minutes to second is:",c*60)

#Even odd factorial

num = int(input("Enter a number:"))



""" Q 2Write a python script to accept a number and check whether it is odd or even.
Also calculates factorial of it. Do not use built-in module functions. """
#check
if num % 2 == 0:
        print('Number is Evern.')
else:
        print('Number is Odd')

f=1
a = int(input("Enter a Number"))
for i in range(1,a+1):
        f=f*i
print("factorial is",f)

'''



""". Q 3Write a python script to accept a number and checks whether it is prime or not.
Do not use built in module functions."""

'''
#Prime or not
n = int(input('Enter the number: '))

if n == 2 or n == 3:
    print("Number is prime")
elif n % 2 == 0:
    print("Not a prime number")
else:
    for i in range(n, 2):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Number is prime")

'''

""" Q 4 rite a python script to accept a number and check whether it is Armstrong
number or not. Do not use built-in module functions."""
#Armstrong number
'''
n=int(input("enter a number "))
sum1=0
temp=n
while temp!=0:
    r=temp%10
    sum1=sum1+(r**3)
    temp=temp//10

if n==sum1:
    print("number is armstrong ")
else:
    print("number is not armstrong ")



    #153 exampl

'''

#5. Write a python script to accept a number and check whether it is palindrome or
#not. Do not use built-in module functions.'''

'''
#6 palindrome of number
n = int(input("Enter the number for palindrome: "))
n1 = n
rev = 0
while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
if rev == n1:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
    #exm 121

    '''


    
    

''' Write a python script to subtract two matrices.
9. 7. Write a python script to add two matrices.'''

'''

r=int(input('Enter the number of row: '))
c=int(input('Enter the number of columns: '))

m1=[]
print('enter the first matrix')
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input('Enter the elements')))
    m1.append(a)
    
#print
for i in range(r):
    print(m1[i])
    
m2=[]
print('enter the 2irst matrix')
for i in range(r):
    b=[]
    for j in range(c):
        b.append(int(input('Enter the elements')))
    m2.append(b)
    
#print
for i in range(r):
    print(m2[i])
    
#addtion of matrix

m3=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(m1[i][j]  m2[i][j])
    m3.append(a)

#resultant matrix
print('Matrix addtion is: ')
for i in range(r):
    print(m3[i])

    '''



"""8. Write a python script to subtract two matrices."""



'''



    '''

'''
#9ite a python script to accept a string and check whether it is palindrome or not.
#lso count the no. of vowels in it.   
 string=input('Enter the string: ')
vowels='aeiouAEIOU'

vowels=sum(1 for char in string if char in vowels)

if string == string[::-1]:
    print('String is palindrome: ')
else:
    print('String is not palindrome: ')
    
print('Count of vowels is: ',vowels)

'''


"""10. Write a python script to accept list elements from user and perform following
operations on it :
a) Sum and multiplication of all the items in a list
b) Largest and smallest number from a list.
c) Second Largest/Smallest number from a list."""


'''
n=int(input('Enter the number of list element'))
l1=[]
print('Enter the list elements: ')
for i in range(1, n+1):
	l1.append(int(input()))
print('list is: ',l1)

#sum
sum=0
for i in l1:
	sum += i
print('Sum is: ',sum)

#multi
mult=1
for i in l1:
	mult=mult*i
print('Multiplication is :',mult)	

#largest
print('Largest number is',max(l1))

#smallest
print('Smallest number is:',min(l1))

#second largest
l1.sort()
print('Second largest number is: ',l1[1])

#second smallest
print('Second smallest number is: ',l1[-2])



'''



#11ite a python script to accept list elements from user for two lists and perform
#following operations on them :
#a) Sort both the list.
#b) Union, intersection and difference of two lists.

'''
# Accepting list elements from the user for List 1
n1 = int(input("Enter the number of elements for List 1: "))
list1 = []
print("Enter the elements for List 1:")
for i in range(n1):
    list1.append(int(input()))

# Accepting list elements from the user for List 2
n2 = int(input("Enter the number of elements for List 2: "))
list2 = []
print("Enter the elements for List 2:")
for i in range(n2):
    list2.append(int(input()))

# Sorting both the lists
list1.sort()
list2.sort()
print("Sorted List 1: ", list1)
print("Sorted List 2: ", list2)

# Union of two lists
union = list(set(list1) | set(list2))
print("Union of two lists: ", union)

# Intersection of two lists
intersection = list(set(list1) & set(list2))
print("Intersection of two lists: ", intersection)

# Difference between two lists
difference = list(set(list1) - set(list2))
print("Difference between List 1 and List 2: ", difference)

'''


"""12. Write a python script to accept tuple elements from user and perform following
operations on it :
a) Accept element from user and add it into the tuple.
b) Convert tuple to a string.
c) Find the repeated elements of a tuple"""


'''

# Accept tuple elements from user
t = tuple(input("Enter tuple elements separated by spaces: ").split())

# Accept element from user and add it into the tuple
new = input("Enter a new element to add to the tuple: ")
t = t + (new,)

# Convert tuple to a string
t_str = str(t)
print("Tuple as a string:", t_str)

# Find repeated elements of a tuple
repeate = set([x for x in t if t.count(x) > 1])
if repeate:
    print("Repeated elements:", repeate)
else:
    print("There are no repeated elements in the tuple.")

   '''


"""13. Write a python script to accept tuple elements from user and perform following
operations on it :
a) Accept a number from user and remove it from the tuple.
b) Accept a position from user and display the element from last of the given
position."""

'''

# Accept tuple elements from user
t = tuple(input("Enter tuple elements separated by spaces: ").split())

# Accept a number from user and remove it from the tuple
num_to_remove = input("Enter a number to remove from the tuple: ")
t = tuple(filter(lambda x: x != num_to_remove, t))

# Accept a position from user and display the element from last of the given position
position = int(input("Enter a position: "))
print("Element from last of the given position:", t[-position])

# Accept a number from user and check whether it is present in a tuple or not
num_to_search = input("Enter a number to search in the tuple: ")
if num_to_search in t:
    print("The number is present in the tuple.")
else:
    print("The number is not present in the tuple.")
 
 '''





""" 14. Write a python script to accept set elements from user and perform following
operations on it :
a) Iterate over given set.
b) Accept a number from user and check if it is present in the given set or not. If
yes then remove it from the set.
c) Accept a number from user and add it into the set."""

'''
s = set()

n = int(input("Enter the number of elements: "))
for i in range(n):
    s.add(int(input("Enter element: ")))

print("Set:", s)

# Iterate over the set
print("Set elements:")
for element in s:
    print(element)

# Accept a number and check if it's present, then remove it
num = int(input("Enter a number to remove: "))
if num in s:
    s.remove(num)
    print("Number removed from set")
else:
    print("Number not found in set")

print("Set after removal:", s)

# Accept a number and add it to the set
num = int(input("Enter a number to add: "))
s.add(num)
print("Set after addition:", s)


'''

# Accept two sets from the user
#15. Write a python script to accept set elements from user for two sets and perform
#following operations on them :
#a) Display set difference.
#b) Create symmetric difference.
#c) Check whether first set is superset of second set or no


'''

set1 = set(input("Enter elements of first set (separated by space): ").split())
set2 = set(input("Enter elements of second set (separated by space): ").split())

# Display set difference
print("Set difference: ", set1 - set2)

# Create symmetric difference
print("Symmetric difference: ", set1 ^ set2)

# Check if first set is superset of second set
if set2.issubset(set1):
    print("First set is a superset of second set")
else:
    print("First set is not a superset of second set")


      '''


'''
 17 .e a python script to accept ‘n’ from user and store the numbers from 1 to n
and its square in first dictionary and numbers from n+1 to 2*n and its cube in
second dictionary. Then concat these two dictionaries and create third dictionary.
For e.g. if n = 5 then,
First dictionary = [1:1,2:4,3:9, 4:16, 5:25]
Second dictionary = [6:216, 7: 343, 8: 512, 9: 729, 10:1000]
Concatenated dictionary = [1:1,2:4,3:9, 4:16, 5:25, 6:216, 7: 343, 8: 512, 9: 729,
10:1000]






n = int(input("Enter a number: "))

# create first dictionary with numbers and their squares
dict1 = {i: i*i for i in range(1, n+1)}

# create second dictionary with numbers from n+1 to 2n and their cubes
dict2 = {i: i*i*i for i in range(n+1, 2*n+1)}

# concatenate both dictionaries to create third dictionary
dict3 = {**dict1, **dict2}

print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Concatenated Dictionary:", dict3)




'''


"""18 .e a python script to accept ‘n’ numbers from user and store them in a singly
linked list. Also print the linked list elements. Use a concept of class"""

'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

n = int(input("Enter the number of elements: "))
lst = LinkedList()
print("Enter the elements:")
for i in range(n):
    lst.insert_at_end(int(input()))
print("The elements in the linked list are:")
lst.print_list()

'''

#Q.19 Write a class Circle in python having radius as attribute with two methods which  

#will compute the area and the circumference of a circle (implement default  

#constructor, parameterised constructor and __str__() function). Write a driver  

#code in which accept a radius from user and making the object of Circle class  

#compute its area and perimeter.  

'''  

class Circle:
	def __init__(self,r):
		self.r=r
		
	def area(self):
		return 3.14*self.r*self.r
	
	def circumference(self):
		return 2*3.14*self.r
		
	def __str__(self):
		return "radius={}".format(self.r)

r=int(input("Enter the radius"))
c=Circle(r)

print('Area of circle is : ',c.area())
print('Circumference of area is : ',c.circumference())		


'''


#Q.22 Write a python class ‘Fraction’ having integer data members numerator and  

#denominator. Define both parameterized and default constructors - __init__  

#method (default values 0 and 1) and __str__() function. Parameterized constructor  

#should store the fraction in reduced form after dividing both numerator and  

#denominator by gcd(greatest common divisor). Write a member function to  

#compute gcd of two integers. Write a driver code in which accept a numerator and  

#denominator from user and create a object of Fraction class 


'''

class fraction: 

    def gcd(self, a, b): 
        if a == b: 
            return a 
        elif a > b: 
            return self.gcd(a - b, b) 
        else: 
            return self.gcd(a, b - a) 

    def __init__(self, num=0, dnum=1): 
        g = self.gcd(num, dnum) 
        self.num = num // g 
        self.dnum = dnum // g 

    def __str__(self): 
        return "{}/{}".format(self.num, self.dnum) 

# Driver code 
num = int(input("Enter the numerator: ")) 
dnum = int(input("Enter the denominator: ")) 

f = fraction(num, dnum) 
print("Fraction:", f)

'''


#Q.24 Create a text file using editor. Write a python script to read this file and count the  

#lines, words, characters in it. 

'''
f1 = open("myfile.txt", "r")
wcnt = 0
ccnt = 0
lcnt = 0

for line in f1:
    lcnt += 1
    ccnt += len(line)
    words = line.split()
    wcnt += len(words)

print("Words in file:", wcnt)
print("Lines in file:", lcnt)
print("Characters in file:", ccnt)

f1.close()

'''

#Q.25 Create a text file using editor. Write a python script to read this file and count the#vowels and consonants in it.  

'''  

f1 = open("myfile.txt", "r")
vcnt = 0
ccnt = 0

for line in f1:
    for word in line.split():
        for char in word:
            if char.isalpha():
                if char in "aeiouAEIOU":
                    vcnt += 1
                else:
                    ccnt += 1

print("Vowels:", vcnt)
print("Consonants:", ccnt)

f1.close()

'''

"""
Q 26 .Create a text file using editor. Write a python script to read this file and convert
upper case to lower case and vice versa and store it into another file.

f1=open('read.txt','r')
f2=open('write.txt','w')

for line in f1:
	for ch in line:
		if ch.islower():
			ch=chr(ord(ch)-32)
			print(ch)
		elif ch.isupper():
			ch=chr(ord(ch)+32)
			print(ch)
		f2.write(ch)
"""

'''
28. Create a database DeptEmp in postgresql. Write a Python script to connect this
database and create Dept and Emp (relationship between Dept and Emp table is
one to many) table within the database.

postgres=# create database mydatabase;
CREATE DATABASE
postgres=# \c mydatabase
You are now connected to database "mydatabase" as user "postgres".
mydatabase=# create table dept(dno int primary, dname varchar(30));
ERROR:  syntax error at or near ","
LINE 1: create table dept(dno int primary, dname varchar(30));
                                         ^
mydatabase=# create table dept(dno int primary key, dname varchar(30));
CREATE TABLE
mydatabase=# insert into dept values(1, 'Pentest');
INSERT 0 1
mydatabase=# insert into dept values(2, 'Web test');
INSERT 0 1
mydatabase=# insert into dept values(3, 'IOT test');
INSERT 0 1
mydatabase=# insert into dept values(4, 'OT test');
INSERT 0 1
mydatabase=# create table emp(eno int primary key, ename varchar(30), salary float, dno int references dept(dno));
CREATE TABLE
mydatabase=# select * from dept
mydatabase-# ;
 dno |  dname   
-----+----------
   1 | Pentest
   2 | Web test
   3 | IOT test
   4 | OT test
(4 rows)

mydatabase=# select * from emp
mydatabase-# ;
 eno | ename | salary | dno 
-----+-------+--------+-----
(0 rows)

mydatabase=# insert into emp values(5, 'Akash',50000,1);
INSERT 0 1
mydatabase=# insert into emp values(5, 'Adesh',60000,2);
ERROR:  duplicate key value violates unique constraint "emp_pkey"
DETAIL:  Key (eno)=(5) already exists.
mydatabase=# insert into emp values(6, 'Adesh',60000,2);
INSERT 0 1
mydatabase=# insert into emp values(7, 'Jatin',60000,3);
INSERT 0 1
mydatabase=# insert into emp values(8, 'Yash',70000,4);
INSERT 0 1
mydatabase=# select * from emp;
 eno | ename | salary | dno 
-----+-------+--------+-----
   5 | Akash |  50000 |   1
   6 | Adesh |  60000 |   2
   7 | Jatin |  60000 |   3
   8 | Yash  |  70000 |   4


import psycopg2
mycon=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
c1=mycon.cursor()
c1.execute('create table dept(dno int primary key,dname varchar (30))')
c1.execute('create table emp(eno int primary key,ename varchar (30),did int references dept(dno))')
mycon.commit()
mycon.close()




29. Create a course(cno, cname, duration) and student(rollno, sname, cno) tables in
postgresql. Relationship between course and student is one to many. Write a
Python script to accept details of student from user and insert that student record
in the student table. Finally selects all rows from the table and display the
record


import psycopg2
mycon=psycopg2.connect(database='mydatabase',user='postgres',password='',host='localhost',port=5432)
c1=mycon.cursor()
c1.execute('select * from course')
data=c1.fetchall()
sid=int(input('Enter student sid: '))
sname=input('Enter student name: ')
print('select course id from the following')
print(data)
cid=int(input('Enter course cid: '))
row=(sid,sname,cid)
c1.execute('insert into student values(%s,%s,%s)',row)
con.commit()
print('Record inserted')
mycon.close()



'''



  
'''


#Q.30  Write a function perfect() which returns True if given number is perfect, otherwise  

#returns False. Use this function to print first n perfect numbers.  

def perfect(n): 

    sum=0 

    for i in range(1,(n//2)+1): 

        if(n%i==0): 

            sum=sum+i 

    if(n==sum): 

        return True 

    else: 

        return False 

#driver code 

  

n=int(input("enter the number:")) 

if (perfect(n)): 

    print("perfect:") 

else: 

    print("not perfect:") 

'''


'''

#Q. 31
Write a menu driven program in python for following operations. (write separate
function for each operation)
a. Max number from the list
b. Min number from the list
c. Sum of all the numbers in a list
d. Multiplication of all the numb
e.exit 
'''
'''

def max1(n):
    return max(n)
def min1(n):
    return min(n)
def sum1(n):
    return sum(n)
def mul(n):
    p=1
    for i in n:
        p=p*i
    return p

n=int(input("enter a number of elements:  "))
l1=[]
for i in range(0,n):
    l1.append(int(input("enter a number s :")))
choice=0
while choice!=5:
    print("1.max\n 2.min\n3.sum\n4.mul\n5.exit")
    choice=int(input("enter a choice : "))
    match choice:
        case 1:
            print ("max of list ",max1(l1))
            break
        case 2:
            print ("min of list",min1(l1))
            break
        case 3:
            print("sum of list ",sum1(l1))
            break
        case 4:
            print("mul of list ",mul(l1))
            break
        case 5:
            print("exit")
            break
        case default:
            print("not found")


'''


#Q. 32
#Write a recursive function sumdigit() to calculate sum of digits of a number.
#Accept a number from user and display sum of its digits

'''
def sum(n):
    if n==0:
        return 0
    return (n%10+sum(int(n/10)))

n=int(input("enter a number "))
print("sum of digit",sum(n))


class NegativeException(Exception):
    msg=''
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return "exception{}".format(self.msg)
try:
    a=int(input("enter a number "))
    if a<0:
        raise(NegativeException("you enter a negative number "))
except NegativeException as error:
    print("error")
else:
    print(a)

'''
'''
Q 33 Write a python script to accept a string and check whether it has a
symbol ‘T’ followed by two to three 'H'. Write regular expression.

import re
s=input("Enter the string: ")
patt="TH{2,3}"

if re.search(patt,s):
        print('Found/matched')
else:
        print("Not found/match")            
       
'''
'''
#34. write a python program containing a possible exception for –ve numbers. Use a try
#block to throw it and a catch block to handle it promptly

class NegEx(Exception):
        msg=''

        def __init__(self,msg):
                self.msg=msg

        def __str__(self):
                return('Exception'+ self.msg)

#main
try:
        a=int(input('Enter any no:'))
        if a<0:
                raise NegEx('Enter negative number')
except NegEx as Error:
        print(Error)

else:
        print(a)
        
'''




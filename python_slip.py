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



""" Write a python script to accept a number and check whether it is odd or even.
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



""". Write a python script to accept a number and checks whether it is prime or not.
Do not use built in module functions."""

'''
#Prime or not
n = int(input('Enter the number: '))

if n == 2 or n == 3:
    print("Number is prime")
elif n % 2 == 0:
    print("Not a prime number")
else:
    for i in range(3, n, 2):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Number is prime")

'''

""" Write a python script to accept a number and check whether it is Armstrong
number or not. Do not use built-in module functions."""
#Armstrong number
'''


n = input("Enter the number for check it is armstrong or not: ")
cnt = 0
for digit in n:
    cnt += 1
no = int(n)
n = no
sum = 0
while no != 0:
    rem = no % 10
    no = no // 10
    sum += rem ** cnt
if n == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
    #153 exampl

'''
	

    '''5. Write a python script to accept a number and check whether it is palindrome or
not. Do not use built-in module functions.'''

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
    #7 tion of two matrix
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# Create the first matrix
m1 = []
print("Enter first matrix:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter element: ")))
    m1.append(a)

# Print the first matrix
for i in range(r):     
    print(m1[i])

# Create the second matrix
m2 = []
print("Enter second matrix:")
for i in range(r):
    b = []
    for j in range(c):
        b.append(int(input("Enter element: ")))
    m2.append(b)

# Print the second matrix
for i in range(r):
    print(m2[i])

# Add the two matrices
m3 = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(m1[i][j] + m2[i][j])
    m3.append(a)

# Print the resulting matrix
print("Matrix Addition =")
for i in range(r):
    print(m3[i])

    '''



"""8. Write a python script to subtract two matrices."""



'''

    #substraction of 2 matrix

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

m1 = []
print("Enter first matrix:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input("Enter element: ")))
    m1.append(a)

for i in range(r):     
    print(m1[i])

m2 = []
print("Enter second matrix:")
for i in range(r):
    b = []
    for j in range(c):
        b.append(int(input("Enter element: ")))
    m2.append(b)

for i in range(r):
    print(m2[i])

m3 = []
for i in range(r):
    a = []
    for j in range(c):
        a.append(m1[i][j]-m2[i][j])
    m3.append(a)

print("Matrix Subtraction =")
for i in range(r):
    print(m3[i])


    '''

'''
#9ite a python script to accept a string and check whether it is palindrome or not.
#lso count the no. of vowels in it.   
s = input("Enter a string: ")
s = s.lower()  # Convert the string to lowercase

# Check if the string is a palindrome
is_palindrome = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Count the number of vowels in the string
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in s:
    if char in vowels:
        count += 1

print("The string contains", count, "vowels")

'''


"""10. Write a python script to accept list elements from user and perform following
operations on it :
a) Sum and multiplication of all the items in a list
b) Largest and smallest number from a list.
c) Second Largest/Smallest number from a list."""


'''
n=int(input('Enter Number of list elements :'))
l1=[]
print("Enter the list Elements :")
for i in range(1,n+1):
    l1.append(int(input()))
print("list is ",l1)

#Sum of list element
sum=0
for i in l1:
   sum+=i
print("Sum is : ",sum)

#Multiplication of list elements
prod=1
for i in l1:
   prod=prod*i
print("Multplication is :",prod)
#smallest elements of list
print("Smallest Element is :",min(l1))

#Largest Element of list 
print("Largest Element is =",max(l1))

#Second Largest/Smallest number form a list
l1.sort()
print("Second Smallest is:",l1[1])
print("Second Largest is:",l1[-2])
#Counting the element
print("count is :",len(l1))


'''


#10. Write a python script to accept list elements from user and perform following
#perations on it :
#a) Sum and multiplication of all the items in a list
#b) Largest and smallest number from a list

'''


n=int(input('Enter Number of list elements :'))
l1=[]
print("Enter the list Elements :")
for i in range(1,n+1):
    l1.append(int(input()))
print("list is ",l1)

#Sum of list element
sum=0
for i in l1:
   sum+=i
print("Sum is : ",sum)

#Multiplication of list elements
prod=1
for i in l1:
   prod=prod*i
print("Multplication is :",prod)
#smallest elements of list
print("Smallest Element is :",min(l1))

#Largest Element of list 
print("Largest Element is =",max(l1))

#Second Largest/Smallest number form a list
l1.sort()
print("Second Smallest is:",l1[1])
print("Second Largest is:",l1[-2])


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

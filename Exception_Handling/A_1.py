
'''

filename = input("Enter the file name: ")
try:
    f1=open('A_1.txt', 'w')
     
except:
    print('Permission denied')


#sudo chmod 000 t1.txt

#f1=input(A_1.py)
'''

a=int(input('1st Number : '))
b=int(input('2st Number : '))

try:
	print('Division = ',a/b)
except ZeroDivisionError:
	 print('You are trying to divide by zero')


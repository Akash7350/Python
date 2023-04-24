
'''	
class NegativeException(Exception):
	msg=""
	def __init__(self, msg):
		self.msg = msg
	def __str__(self):
		return('Exception: ' + self.msg)

try:
	a = int(input('Enter a number: '))
	
	if a < 0:
		raise NegativeException('You have entered a negative number')
except NegativeException as error:
	print(error)
else:
	print(a)

'''
#q2 write a program containing a possible exception for number > 500 use a try block to throw it and a ctach block to handle it promptly 

class NumberTooLargeException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "NumberTooLargeException: " + self.message

try:
    num = int(input("Enter a number: "))
    if num > 500:
        raise NumberTooLargeException("The number is too large!")
except NumberTooLargeException as e:
    print(e)
else:
    print("The number is:", num)


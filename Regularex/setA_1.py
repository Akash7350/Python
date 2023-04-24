#Exercise 	//Regular Expressions

''' import re
s1 = input('Enter the String : ')

#pattern = re.compile('[A-Z]''[a-z]+') 2 question

pattern = re.compile('I[A-Za-z0-9]+A') #Q.4th


if pattern.match(s1):
	print('Mathch Found')
else:
	print("Please Enter Only Alphabets and digits")
	


	
#Q1 To check if a string contains only a certain set of characters (in this case o-z, A-Z, and 0-9) in Python	

import re

s1 = input('Enter the String: ')
pattern = re.compile('^[o-zA-Z0-9]+$')

if pattern.match(s1):
    print('Match Found')
else:
    print('Please Enter Only Alphabets and digits between o-z, A-Z, and 0-9')

	
#4 Question match a string that has an 'I' followed by anything, ending in 'A' python program 
import re

s1 = input('Enter the String: ')
pattern = re.compile('I[A-Za-z0-9]+A')

if pattern.match(s1):
    print('Match Found')
else:
    print('No match found')
    


#Question 5th     
import re

ip_address = input('Enter the IP address: ')

# Use a regular expression pattern to remove leading zeros from each component
ip_address = re.sub(r'\b0+(\d)', r'\1', ip_address)

print('IP address with leading zeros removed:', ip_address)

     
   
'''
#Question 5th    
import re

text = 'The quick brown fox jumps over the lazy dog.'
words_to_search = ['fox', 'dog', 'horse']

for word in words_to_search:
    pattern = re.compile(re.escape(word))
    match = pattern.search(text)
    if match:
        print(f"'{word}' found at position {match.start()} in the text.")
    else:
        print(f"'{word}' not found in the text.")
'''
 
 

    
    
    
    


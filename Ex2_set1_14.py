n=int(input("Enter  a String"))
vowels=0
consonants=0

for char in n:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels +=1
        else:
            consonants +=1

print("Number of vowels: ",vowels)
print("Number of consonants",consonants)

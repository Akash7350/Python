import random,itertools
deck = list(itertools.product(range(1,14),['Diamond','Spade','Heart','Club']))
random.shuffle(deck)
#for i in range(0,52):
 #   print(deck[i])
n = int(input("Enter the card number to guess: 0-51 --"))
print(deck[n])

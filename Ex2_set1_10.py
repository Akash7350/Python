import random,itertools

deck=list(itertools.product(range(1,14), ["Diamonds", "Spades", "Heart", "club"]))
random.shuffle(deck)
#for i in range(0, 52):
 #   print(deck[i])
n=int(input("Enter the card to guess 0 to 51 :"))
print("Your card is",deck[n])

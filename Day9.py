
import os
print(''''
  _________________.---.______
 (_(______________(_o o_(____()
              .___.'. .'.___.
              \ o    Y    o /
               \ \__   __/ /
                '.__'-'__.'
                    '''
'')

# Introductory message
print("Welcome to the secret aution program")

bidders = []
num = 0
highest_bid = 0
bidder_number = 0
other_bidders = True
 
while other_bidders == True:
    os.system('cls')
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    if bid > highest_bid:
        highest_bid = bid
        bidder_number = num
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ") 
    if other_bidders == "yes":
        other_bidders = True
    else:
        other_bidders = False
    num += 1
    bidders.append({"name": name, "bid": bid})
        
print(bidders)

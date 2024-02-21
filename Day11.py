
import random
resume = False 
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start_game == 'y':
    resume = True
else: resume = False

while resume == True:
    print(
    """
 .------..------.    ____  _            _        _            _    
 |A.--. ||K.--. |   |  _ \| |          | |      | |          | |   
 | (\/) || :/\: |   | |_) | | __ _  ___| | __   | | __ _  ___| | __
 | :\/: || :\/: |   |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
 | '--'A|| '--'C|   | |_) | | (_| | (__|   < |__| | (_| | (__|   < 
 |------||------|   |____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\\
 `------'`------'                                               

    """
    )

    def card():
        card_list = []
        for i in range(1, 3):
            a = random.randint(1, 11)
            card_list.append(a)
            b = random.randint(1, 11)
            card_list.append(b)
            print(f"Your cards: {card_list}")

    computer_card = random.randint(1, 11)
    print(f("Computer's first card: {computer_card}"))
    resume = False


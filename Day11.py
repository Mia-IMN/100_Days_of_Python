
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

    def first_two_cards():
        card_list = []
        for i in range(1, 3):
            a = random.randint(1, 11)
            card_list.append(a)
            b = random.randint(1, 11)
            card_list.append(b)
            return(f"Your cards: {card_list}")
    players_card = first_two_card()
    print(players_card)
    
    def card():
        random.randint(1, 11)
    computers_card = card()
    print(f"Computer's first card: {computers_card}")

    continue = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue == 'y':
        players_next_card = card()
    else:
        print(f"Your final hand: {players_card}")

    resume = False


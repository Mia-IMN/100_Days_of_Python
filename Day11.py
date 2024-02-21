
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
    
    def winner(player, computer):
        players_score = 0
        computer_score = 0
        for i in player:
            players_score += i
        for i in computer:
            computer_score += i
        if players_score > computer_score:
            if players_score <= 21:
                print("You win")
        else: print("You lose")
        

    def first_two_cards():
        card_list = []
        for i in range(1, 3):
            a = random.randint(1, 10)
            card_list.append(a)
            b = random.randint(1, 10)
            card_list.append(b)
            return card_list
    
    players_card = first_two_cards()
    print(f"Your cards: {players_card}")
    
    def card():
        return random.randint(1, 10)

    
    computers_first_card = card()
    print(f"Computer's first card: {computers_first_card}")

    computers_total_card = []
    computers_total_card.append(computers_first_card)
    
    computers_second_card = card()
    computers_total_card.append(computers_second_card)

    continue_game = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_game == 'y':
        players_next_card = card()
    else:
        print(f"Your final hand: {players_card}")
        print(f"Computer's final hand: {computers_total_card}")
        winner(players_card, computers_total_card)


    resume = False


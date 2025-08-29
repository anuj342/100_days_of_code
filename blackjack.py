import random

skeleton = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/ """

def blackjack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_cards = []
    dealer_cards = []
    choice = input("Do you want to play blackjack? (y/n):")
    while choice == "y":
        print(skeleton)
        user_cards = random.sample(cards, 2)
        dealer_cards = random.sample(cards, 2)
        print(f"Your cards are: {user_cards}")
        print(f"The sum of your cards are: {sum(user_cards)}")
        print(f"The dealer's first card are: {dealer_cards[0]}")

        add_card = input("Do you want to add another card? (y/n):")
        if add_card == "y":
            user_cards.append(random.choice(cards))
            print(f"The sum of your cards are: {sum(user_cards)}")
            dealer_cards.append(random.choice(cards))
        else:
            print(f"The sum of your cards are: {sum(user_cards)}")
            print(f"The dealer's first card are: {dealer_cards[0]}")
            print(f"The sum of dealers cards are: {sum(dealer_cards)}")
            if sum(user_cards) < sum(dealer_cards):
                print("Dealer wins!")
            elif sum(user_cards) > sum(dealer_cards):
                print("User wins!")
            elif sum(user_cards) == 21 and sum(dealer_cards) == 21:
                print("You win")
            else:
                print("Error")
            break

blackjack()
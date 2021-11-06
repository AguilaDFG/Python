############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
player_cards = []
dealer_cards = []
dealer_cards_hidden = []
def deal_card():
    card = random.choice(cards)
    return card
def eleven_to_one(hand):
    hand.remove(11)
    hand.append(1)
def blackjack(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return True
print(logo)
player_cards.append(deal_card())
dealer_cards.append(deal_card())
dealer_cards_hidden.append(dealer_cards[0])
print(f"Your cards: {player_cards}")
print(f"Dealer's cards: {dealer_cards_hidden}")
next = True
while next:
    want_card = input("Dou you want a card? Type Y or N: ").lower()
    if want_card == "y":
        player_cards.append(deal_card())
        print(f"Your cards: {player_cards}")
        if blackjack(player_cards):
            print("Blackjack! You win")
        if sum(player_cards) > 21 and not 11 in player_cards:
            print("You lose")
            next = False
        elif sum(player_cards) > 21 and  11 in player_cards:
            eleven_to_one(player_cards)
        if sum(dealer_cards) < 17 and next:
            dealer_cards.append(deal_card())
            dealer_cards_hidden.append("?")
            print(f"Dealer's cards: {dealer_cards_hidden}")
    else:
        print(player_cards)
        while sum(dealer_cards) < 17:
            dealer_cards.append(deal_card())
            dealer_cards_hidden.append("?")
            print(f"Dealer's cards: {dealer_cards_hidden}")
            if sum(dealer_cards) > 21 and 11 in dealer_cards:
                eleven_to_one(dealer_cards)
        print(f"Dealer's cards: {dealer_cards}")
        if blackjack(dealer_cards):
            print("Dealer Blackjack! You lose")
        if sum(dealer_cards) > 21:
            print("You win")
        elif sum(player_cards) > sum(dealer_cards):
            print("You win")
        elif sum(player_cards) < sum(dealer_cards):
            print("You lose")
        else:
            print("Draw")
        next = False






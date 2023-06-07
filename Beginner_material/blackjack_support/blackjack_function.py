import random
# from LearningPy11 import user_total, dealer_total
from random import randint

card_value = ['A', '2', '3', '4', '5',
              '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# card_type = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_type = ['♥', '♦', '♣', '♠']
decks = []


def card_decks():
    for value in card_value:
        for type in card_type:
            decks.append(value + type)
    return decks


card_decks()


def card_value(card):
    if card[0] in ['J', 'Q', 'K', '1']:
        return int(10)
    elif card[0] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        return int(card[0])
    elif card[0] == 'A':
        print("\n" + str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num != '1' or num != '11':

            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n")


def deal_cards():
    """Draw cards"""
    cards = random.choice(decks)
    decks.remove(cards)
    return cards


def final_result(dealer_total, user_total):
    if dealer_total == 21 and user_total == 21:
        return "Push! It's a tie. 🧐"
    elif dealer_total == 21:
        return "Dealer wins with a Blackjack! 🤬"
    elif user_total == 21:
        return "You win with a Blackjack! 🤑"
    elif dealer_total > 21:
        return "Dealer busts. You win! 😎"
    elif user_total > 21:
        return "You bust. Dealer wins! 😰"
    elif dealer_total > user_total:
        return "Dealer wins! 😭"
    elif user_total > dealer_total:
        return "You win! 😏"
    else:
        return "Push! It's a tie. 😶‍🌫️"


def ask_to_play_again():
    play_again = input("\nWould you like to continue? (y/n): ")
    return play_again == "y"

# BLACKJACK / 21 CAPSTONE PROJECT
import random
from random import randint
from blackjack_support.blackjack_function import card_value, deal_cards, final_result
from blackjack_support.logo import logo
import os
def cls(): return os.system('cls')


play_again = 'y'

while play_again == 'y':
    print(logo)
    user_cards = []
    dealer_cards = []
    is_blackjack = False
    for _ in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    user_total = 0
    for val in user_cards:
        user_total += (card_value(val))
    dealer_total = 0
    for val in dealer_cards:
        dealer_total += (card_value(val))

    if user_total == 21:
        print("You Win, Blackjack! 😃")
        print(
            f"Your final hand: {user_cards}, final score: {user_total}")
        print(
            f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")
        play_again = input("\nWould you like to continue? (y/n): ")
        break
    elif dealer_total == 21:
        print("Lose, opponent has Blackjack 😱!")
        print(
            f"Your final hand: {user_cards}, final score: {user_total}")
        print(
            f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")
        play_again = input("\nWould you like to continue? (y/n): ")

        break
    if play_again != 'y':
        break
    else:
        while is_blackjack == False:
            user_turn = True
            print(user_cards)
            print(f"Your current total is: {user_total}")
            print(f"Computer's first card: '[ {dealer_cards[0]} ]'")

            while user_turn == True:
                user_answer = input(
                    'Would you like to hit or stand?\n "1" For Hit\n "2" For Stand\n')
                if user_answer == "1":

                    new_cards = deal_cards()
                    user_cards.append(new_cards)
                    user_total = sum(card_value(card) for card in user_cards)
                    print(user_cards)
                    print(f"Now Your current total is: {user_total}")

                    if user_total > 21:
                        final_result(dealer_total, user_total)

                        break

                elif user_answer == "2":
                    user_turn = False
                    break

            while dealer_total < 17 and user_total < 21:
                print("The Dealer Hits again")
                new_cards = deal_cards()
                dealer_cards.append(new_cards)
                dealer_total = sum(card_value(card)
                                   for card in dealer_cards)
                continue
            result = final_result(dealer_total, user_total)
            print(result)
            print(
                f"Your final hand: {user_cards}, final score: {user_total}")
            print(
                f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")

            break
    play_again = input("\nWould you like to play again? (y/n): ")

    if play_again != 'y':
        print("Thank you for playing!")
        break
    # elif play_again == "y":
    #     continue

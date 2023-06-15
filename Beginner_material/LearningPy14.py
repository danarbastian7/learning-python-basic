# HIGHER LOWER GAME
import os
from higherlower_game_support.data import data
from higherlower_game_support.logo import logo, vs
import random
def cls(): return os.system('cls')


def compare_data(a, b):
    """Use if statement to compare the data"""
    while True:
        answer = input("Who has more followers? Type 'A' or 'B'\n").lower()
        if answer == 'a':
            if a > b:
                return True
            else:
                return False
        elif answer == 'b':
            if b > a:
                return True
            else:
                return False
        else:
            print("Invalid input. Please enter 'A' or 'B'.")


play_on = True
final_score = 0
os.system('cls' if os.name == 'nt' else 'clear')
while play_on:

    a_figure = random.choice(data)
    data_without_a = [figure for figure in data if figure != a_figure]
    b_figure = random.choice(data_without_a)
    print("Higher Lower Game has been started!")

    print(
        f"{a_figure['name']}, is a {a_figure['description']} from {a_figure['country']}")
    print(vs)
    print(
        f"{b_figure['name']}, is a {b_figure['description']} from {b_figure['country']}\n")

    comparison = compare_data(
        a_figure['follower_count'], b_figure['follower_count'])

    if comparison == True:
        final_score += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        play_on = True
        print(f"You are right! Current score: {final_score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        play_on = False
        break

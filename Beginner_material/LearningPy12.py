# Local Vs Global Scope
# enemies = 1

# Local Scope
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# # Enemies will equal to 2


# increase_enemies()
# print(f"enemies outside function: {enemies}")
# # Enemies will equal to 1

# Global Scope
# player_health = 10


# def game():
#     def drink_potion():
#         # Local Variable
#         potion_strength = 2
#         print(player_health)
#     drink_potion()


# game()
# =============
# There is no block scope
# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

#  ==========
# Modifying Global Scope
# enemies = 1


# def increase_enemies():
#     # Use 'global' to call global scope
#     # global enemies
#     # enemies += 1
#     # or
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"Enemies inside function: {enemies}")


# Global Constants
# USE UPPERCASE

# PI = 3.1459
# URL = "http://www.google.com"


# def calc():
#     return PI * 2

# ===========================
# The Number Guessing Game
import random
from guess_number_support.guess_number_function import guess, guess_remain, asking_user, ask_to_play_again, search_dif
n = 100
n_output = []


play_on = True

while play_on == True:
    for i in range(1, n+1):
        n_output.append(i)
    print("Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100")
    level_input = int(input(
        "Choose a difficulty. Type '1', '2', or '3'.\n1. Easy\n2. Medium\n3. Hard\n"))
    guess_attempt = guess(lvl=level_input)
    print(f'You have {guess_attempt} attempts remaining to guess the number')

    attempt = True
    random_num = random.choice(n_output)
    while attempt:
        if guess_attempt > 0:

            answer = asking_user()
            print(random_num)
            if asking_user:
                guess_attempt = guess_remain(guess=guess_attempt)
                difference = search_dif(answer, random_num)
                print(f"\n{difference}\n")

            if answer == random_num:
                print(f"You got it! The answer was {answer}")
                attempt = False

                break

            print(
                f'You have {guess_attempt} attempts remaining to guess the number')

        else:
            print("You lose")
            attempt = False
    play_on = ask_to_play_again()
    # if play_on != True
    #     print("Thank you for playing!")
    #     break

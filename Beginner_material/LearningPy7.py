# HANGMAN PROJECT

import os

import random
from hangman_support.HangmanLogo import logo
from hangman_support.word_list import word_list
from hangman_support.stages import stages


lives = len(stages) - 1
def cls(): return os.system('cls')


answer = False
count = 0
word_choose = list(random.choice(word_list).lower())
word_guess = (["_"] * len(word_choose))
previous_choose = ""

print(f"{logo}\nPssst, the solution is thriftless")
print(' '.join(map(str, word_guess)))


while "_" in word_guess:

    guess_input = input("What is your guess?\n").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    count += 1

    if count > 1 and guess_input in previous_choose:
        print("Input must be different from the previous input")
        print(stages[lives])
        print(' '.join(map(str, word_guess)))
        continue

    previous_choose += guess_input
    for i in range(len(word_choose)):
        if guess_input == word_choose[i]:
            word_guess[i] = guess_input

            answer = True

    if not answer:
        lives -= 1
        print(
            f"You guess {guess_input}, that's not in the word. You lose a life.")
        if lives == 0:

            print("You Lose")
            print(f"The correct answer is {''.join(map(str, word_choose))}")
            print(stages[lives])
            break
    elif answer == True:
        print(
            f"Correct! You choose the correct alphabet, that is ", guess_input, "")

    print(stages[lives])
    if (word_choose == word_guess):
        print("You win")
        print(f"Your word is {''.join(map(str, word_choose))}")
        print(stages[lives])
        break
    answer = False

    print(' '.join(map(str, word_guess)))

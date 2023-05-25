# HANGMAN PROJECT

import random
from HangmanLogo import logo
import os

word_list = ["Albania", "Andorra", "Argentina", "Armenia", "Australia",
             "Austria", "Belarus", "Belgium", "Bolivia", "Botswana",
             "Brazil", "Bulgaria", "Cambodia", "Cameroon", "Canada",
             "Colombia", "Croatia", "Denmark", "Dominica", "Ecuador",
             "Estonia", "Ethiopia", "Finland", "Georgia", "Germany",
             "Grenada", "Guatemala", "Honduras", "Hungary", "Iceland",
             "Indonesia", "Ireland", "Jamaica", "Kazakhstan", "Kenya",
             "Kiribati", "Kyrgyzstan", "Lithuania", "Luxembourg", "Malaysia",
             "Maldives", "Mauritania", "Moldova", "Mongolia", "Montenegro",
             "Mozambique", "Namibia", "Nicaragua", "Nigeria", "Pakistan",
             "Paraguay", "Philippines", "Portugal", "Romania", "Rwanda",
             "Slovakia", "Slovenia", "Somalia", "Suriname", "Tanzania",
             "Thailand", "Tunisia", "Turkey", "Uganda", "Uruguay",
             "Uzbekistan", "Venezuela", "Vietnam", "Zimbabwe"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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
    # print(count)
    if count > 1 and guess_input in previous_choose:
        print("Input must be different from the previous input")
        print(stages[lives])
        print(' '.join(map(str, word_guess)))
        continue

    # print(previous_choose)
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

# HANGMAN PROJECT

import random
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
answer = False


count = -1
word_choose = list(random.choice(word_list).lower())

word_guess = (["_"] * len(word_choose))
print(word_guess)


while "_" in word_guess:

    guess_input = input("What is your guess? ").lower()

    for i in range(len(word_choose)):
        if guess_input == word_choose[i]:
            word_guess[i] = guess_input
            answer = True

    if not answer:
        lives -= 1
        if lives == 0:
            print("You Lose")
            print(f"The correct answer is{word_choose}")
            print(stages[lives])
            break
    print(stages[lives])
    if (word_choose == word_guess):
        print("You win")
        print(f"Your word is{word_choose}")
        print(stages[lives])
        break
    answer = False

    # print(answer)
    print(word_guess)
    # print(word_choose)

# RANDOMIZATION AND PYTHON LISTS
import random


# random_integer = random.randint(1, 100)
# print(random_integer)

# random_float = random.random()
# # If we want generate a number 0,0000 - 5,0000
# random_float2 = random.random() * 5
# print(random_float2)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# =============================

# HEAD OF TAILS
# random_choose = random.randint(1, 2)
# if random_choose == "1":
#     print("Head")
# else:
#     print("Tails")

# =========================

# LISTS DATA STRUCTURE

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
#                      "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # states_of_america.append("Angelaland")
# states_of_america.extend(["Angelaland", "Westland"])

# # print(states_of_america[2])
# # print(states_of_america[-1])
# print(states_of_america)

# ================================

# names_string = input("Give me everybody's name, separated by a comma.\n")
# names = names_string.split(",")
# # random_name = random.choice(names).capitalize()\
# num_items = len(names)
# random_number = random.randint(0, num_items-1)


# # print(f"{random_name} is going to buy the meal today!")
# print(f"{names[random_number].capitalize()} is going to buy the meal today!")

# =====================
# NESTED LISTS

# fruits = ["Strawberries", "Nectarines", "Apples", "Peaches"]
# vegetables = ["Spinach", "Kale", "Tomato", "Celery"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)


# ==================================

# TREASURE MAP

# row1 = ["😃", "😅", "😛"]
# row2 = ["😳", "🥵", "🤯"]
# row3 = ["👺", "🤩", "🥳"]

# map = [row1, row2, row3]
# position = input("Where do you want to put the treasure? ")


# horizontal = int(position[0])
# vertical = int(position[1])

# map[vertical - 1][horizontal - 1] = "X"


# print(f"{row1}\n{row2}\n{row3}")
# print(selected_row)

# ============================

# ROCK PAPER SCISSORS

name_input = input("What's your name?\n")


user_input = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


com_input = random.randint(0, 2)
if user_input < (len(game_images) - 1):
    print(game_images[user_input])
    print(f"Computer choose:\n{game_images[com_input]}")
else:
    print("Please input the correct value")
# print(len(game_images))


if user_input == com_input:
    print(f"Both player selected same. It's a tie!")
elif user_input == 0:
    if com_input == 2:
        print(f"Rock smashes scissors!\n {name_input} win! ")

    else:
        print(f"Paper covers rock! \n {name_input} lose! ")

elif user_input == 1:
    if com_input == 0:
        print(f"Paper covers rock! \n {name_input} win")

    else:
        print(f"Scissors cuts paper! \n {name_input} lose! ")

elif user_input == 2:
    if com_input == 1:
        print(f"Scissors cuts paper! \n {name_input} win ")

    else:
        print(f"Rock smashes scissors! \n {name_input} lose! ")

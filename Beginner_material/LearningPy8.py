# FUNCTION WITH INPUT

# def greet():
#     hello = input("What's your greeting?\n")
#     name = input("What's your name?\n")
#     print(hello + " " + name)


# greet()

# FUNCTION THAT ALLOWS FOR INPUT
# def gree_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")


# gree_with_name("Jack")

# FUNCTIONS WITH MORE THAN 1 INPUT

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is the weather in {location}")


# greet_with(name="jack", location="auckland")

# =======================
# PAINT AREA CALCULATOR

# import math


# test_h = int(input("Heigh of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5


# def paint_calculator(height, width, cover):
#     number_of_cans = (test_h * test_w) / coverage
#     print(f"You'll need {math.ceil(number_of_cans)} number of cans")


# paint_calculator(height=test_h, width=test_w, cover=coverage)

# =============================
# PRIME NUMBER CHECKER

# n = int(input("Check this number: "))


# def prime_checker(number):
#     if number < 2:
#         print(f"This {number} is not a prime number.")
#     result = 0
#     for i in range(2, number):
#         if number % i == 0:
#             result += 1
#     if result == 0:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")


# prime_checker(number=n)

# ANOTHER SOLUTION
# def prime_checker(number=n):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")


# prime_checker(n)

# =========================
# FINAL PROJECT CAESAR CIPHER
import math
from caesar_chiper_support.art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


# def encrypt(t, s):

#     new_words = ""
#     for char in t:
#         if char in alphabet:
#             index = alphabet.index(char)
#             index += s

#             if index > 25:
#                 index = index - 26
#                 new_words += alphabet[index]
#             else:
#                 new_words += alphabet[index]

#     print(f"The encoded text is {new_words}")


# def decrypt(t, s):
#     print("Welcome to decode")
#     new_words = ""
#     for char in t:
#         if char in alphabet:
#             index = alphabet.index(char)
#             index -= s
#             if index < 0:
#                 index = index + 26
#                 new_words += alphabet[index]
#             else:
#                 new_words += alphabet[index]
#     print(f"The decoded text is {new_words}")


# def run_code():
#     if direction == "1":
#         encrypt(t=text, s=shift)
#     elif direction == "2":
#         decrypt(t=text, s=shift)
#     else:
#         print("Input the correct number")


def cipher_text(t, s, d):
    new_words = ""

    for char in t:
        if char in alphabet:
            if d == "1":
                new_i = 0

                index = alphabet.index(char)
                new_i = index + s

                while new_i > 25:
                    new_i -= 26
                    continue
                new_words += alphabet[new_i]

            elif d == "2":
                new_i = 0

                index = alphabet.index(char)
                new_i = index - s
                while new_i < 0:
                    new_i += 26
                    continue
                new_words += alphabet[new_i]

        else:
            new_words += char

    if d == "1":
        print(f"The encoded text is {new_words}")
    elif d == "2":
        print(f"The decoded text is {new_words}")
    else:
        print("Please input the correct input.")


def do_cipher():
    while True:
        direction = input("Type 1 to encrypt, type 2 to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cipher = cipher_text(t=text, s=shift, d=direction)
        restart_choice = input("Do you want to restart the program? (y/n) ")
        if restart_choice == "y":
            continue
        else:
            print("Goodbye")
            break


do_cipher()

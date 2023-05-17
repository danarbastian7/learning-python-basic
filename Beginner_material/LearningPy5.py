# PYTHON LOOPS

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")
# print(fruits)


# ============================
# STUDENTS HEIGHT AVERAGE

# students_heights = input("Input a list of student heights ").split()

# for n in range(0, len(students_heights)):
#     students_heights[n] = int(students_heights[n])
# # print(students_heights)
# total_height = 0
# for height in students_heights:
#     total_height += height

# number_of_students = 0
# for student in students_heights:
#     number_of_students += 1

# average = total_height / number_of_students
# # print(student_height)
# print(f"Your average height is {average}")

# =====================
# STUDENTS SCORES
# students_scores = input("Input a list of students score ").split()

# for n in range(0, len(students_scores)):
#     students_scores[n] = int(students_scores[n])

# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score

# print(f"The highest score in the class is: {max_score}")

# =====================
# For Loop Range Function
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# ================================
# ODD NUMBER

# total_odd_number = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total_odd_number += number
# print(f"The total odd number is {total_odd_number}")

# ================================
# FIZZ BUZZ

# range1 = int(input("Input the first range: "))
# range2 = int(input("Input the second range: "))

# for number in range(range1, range2):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# ================================
# PASSWORD GENERATOR (FINAL PROJECT)


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 1
# password_generator = []

# random_number = random.choice(numbers)
# random_symbol = random.choice(symbols)
# random_letter = random.choice(letters)


# for number in range(nr_numbers):
#     random_number = random.choice(numbers)
#     password_generator += random_number
# for symbol in range(nr_symbols):
#     random_symbol = random.choice(symbols)
#     password_generator += random_symbol
# for letter in range(nr_letters):
#     random_letter = random.choice(letters)
#     password_generator += random_letter

# random.shuffle(password_generator)
# # result_password = ''.join(password_generator)
# result_password = ""
# for result in password_generator:
#     result_password += result

# print(result_password)

# 2
password = []
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

result = ""
random.shuffle(password)
for result_pass in password:
    result += result_pass

print(f"Your password is: {result}")

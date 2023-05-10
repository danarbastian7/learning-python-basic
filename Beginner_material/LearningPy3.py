#### DAY 3 (CONDITIONAL STATEMENTS, LOGICAL OPERATORS, CODE BLOCKS, ADN SCOPE)

# ============================
# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ======================
# ODD OR EVEN NUMBER
# print("Welcome to Odd or Even Number!")
# number_input = int(input("Please input a number: "))

# if (number_input % 2) == 1:
#     print("This is an Odd Number")
# else:
#     print("This is an Even Number")

# =============================
# IF AND ELIF CONDITIONS

# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age > 18:
#         print("Please pay $12")
#     elif age <= 18 and age >= 12:
#         print("Please pay $7")
#     elif age < 12:
#         print("Please pay $5")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# ====================================
# BMI AND THE CONCLUSION

# input_height = input("Enter your height in m: ")
# input_weight = (input("Enter your weight in kg: "))
# height = float((input_height))
# weight = float((input_weight))
# bmi_val = float(round(weight/(height ** 2), 2))
# bmi_res = ""

# if bmi_val <= 18.5:
#     bmi_res = "Underweight"
# elif bmi_val > 18.5 and bmi_val <= 25:
#     bmi_res = "Normal weight"
# elif bmi_val > 25 and bmi_val <= 30:
#     bmi_res = "Overweight"
# elif bmi_val > 30 and bmi_val <= 35:
#     bmi_res = "Obese"
# elif bmi_val > 35:
#     bmi_res = "Clinically obese"




# print(f"Your BMI is {bmi_val}, you are {bmi_res}")

# ================================
# LEAP YEAR OR NOT A LEAP YEAR

# leap_year_input = int(input("Which year you want to check? "))
# leap_year_res = ""

# if leap_year_input % 4 == 0:
#     print("Leap year")
#     if leap_year_input % 100 != 0:
#         leap_year_res ="Leap year"
#     else:
#         leap_year_res ="Not a leap year"
#         if leap_year_input % 400 == 0:
#              leap_year_res ="Leap year"
#         else:
#             leap_year_res ="Not a leap year"
# else:
#  leap_year_res ="Not a leap year"

# print(f"{leap_year_input} is {leap_year_res}")

# ======================
# MULTIPLE IF

# print("Welcome to the rollercoaster!")

# height = int(input("What is your height in cm? "))
# total_bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age >= 45 and age <= 55:
#         total_bill += 0
#     elif age > 18 and age <45:
#       total_bill += 12
#     elif age <= 18 and age >= 12:
#        total_bill += 7
#     elif age < 12:
#      total_bill += 5
#     wants_photo = input("Do you want a photo taken? Y or N. ").upper()
#     if wants_photo == "Y":
#       total_bill += 3
#     else:
#        total_bill += 0
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# print(f"Your total bill is ${total_bill}.")

# =============================
# PIZZA SHOP

# print("Welcome to Pizza Shop!")

# total_price = 0
# pizza_size = input("What size you want to order? L / M / S ").upper()
# if pizza_size == "S":
#     total_price += 15
# elif pizza_size == "M":
#     total_price += 20
# elif pizza_size == "L":
#     total_price += 25
# else:
#     print("Sorry, that size is not available.")

# add_pepperoni = input("Do you want to add pepperoni? Y / N ").upper()
# if add_pepperoni == "Y":
#     if pizza_size == "S":
#      total_price += 2
#     elif pizza_size == "L" or pizza_size == "M":
#      total_price += 3

# extra_cheese = input("Do you want extra cheese? Y / N ").upper()
# if extra_cheese == "Y":
#     total_price += 1

# print(f"Your final bill is: ${total_price}")

# ========================
#LOVE CALCULATOR

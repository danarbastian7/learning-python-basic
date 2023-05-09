#PRIMITIVE DATA TYPES

#String
# print("Hello"[0])
# print("123" + "345")

#Integer
# print(123 + 345)
# print(123_34)

#Float (Decimal)
# 3.14

#Boolean
#True or False

#===========================
# num_char = len(input("What is your name? "))
# num_char_str = str(num_char)
# print("Your name is " + num_char_str + " character" )

# print(type(num_char)) --> to know what is the data type of variable
# print("Your name is " + num_char.__str__() + " character" )
# print(70 + float("134.5"))

# two_digit_number = input("Two digit number\n")

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# print("Your total number is", first_digit + second_digit)

###### Mathematical Operations
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3

# print(3 * (3 + 3) / 3 - 3)

########### BMI Calculate

# input_height = input("Enter your height in m: ")
# input_weight = (input("Enter your weight in kg: "))
# height = float((input_height))
# weight = float((input_weight))
# # print(type(height))

# print("Here is your BMI:", +  round(weight/(height ** 2), 0))

##### NUMBER MANIPULATIONS AND F STRING
# print(round(8/3))
#if you want decimal behind coma
# print(round(8/3, 2))
# print(type(4/2))

# score = 2
# height = 1.8
# isWinning = True
# #f-String

# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

###### CHALLENGE LIFE IN WEEKS

#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months

# age = input("What is your current age? ")

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12


# message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {years_remaining} months left"
# print(message)

##### FINAL PROJECT = TIP CALCULATOR

bill_input = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
percentage_tip_input = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_input = int(input("How many people to split the bill? "))



total_bill = ((bill_input) * (100 + (percentage_tip_input ) ) /100)
split_bill = total_bill / (split_input)


print(f"Each person should pay: ${round(split_bill, 2)}")
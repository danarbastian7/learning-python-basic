# FUNCTIONS WITH OUTPUTS


# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return

#     formatted_f_name = (f_name.title())
#     formatted_l_name = (l_name.title())
#     return (f"{formatted_f_name} {formatted_l_name}")


# print(format_name("ANGela", "YUU"))
# print(format_name(input("What is your first name? "),
#       input("What is your last name? ")))


# Days in Month =====================

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(y, m):
#     if m > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if is_leap(y) and month == 2:
#         return 29
#     return month_days[m-1]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(y=year, m=month)
# print(days)

# Docstrings ==============================

# def format_name(f_name, l_name):

#     """Take a first ang last name and format it to return the titcle case version of the name."""
#     if f_name == "" or l_name == "":
#         return

#     formatted_f_name = (f_name.title())
#     formatted_l_name = (l_name.title())
#     return (f"{formatted_f_name} {formatted_l_name}")

# format_name()

# CALCULATE PROGRAM =========================
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers


def subtract(x, y):
    return x - y

# This function multiplies two numbers


def multiply(x, y):
    return x * y

# This function divides two numbers


def divide(x, y):
    return x / y


print("+ \n-\n*\n/ ")


should_restart = True
num1 = int(input("What's the first number? "))
result = num1
result2 = 0
is_first = True
while True:

    operation_choose = input("Pick an operation: ")
    if operation_choose in ('+', "-", "*", "/"):
        num2 = int(input("What's the next number? "))
        if operation_choose == "+":
            result2 = result
            result = add(result, num2)
            if is_first == True:
                print(f"{num1} + {num2} = {result}")
                is_first = False
            else:
                print(f"{result2} + {num2} = {result}")
        elif operation_choose == "-":
            result2 = result
            result = subtract(result, num2)
            if is_first == True:
                print(f"{num1} - {num2} = {result}")
                is_first = False
            else:
                print(f"{result2} - {num2} = {result}")
        elif operation_choose == "*":
            result2 = result
            result = multiply(result, num2)
            if is_first == True:
                print(f"{num1} * {num2} = {result}")
                is_first = False
            else:
                print(f"{result2} * {num2} = {result}")
        elif operation_choose == "/":
            result2 = result
            result = divide(result, num2)
            if is_first == True:
                print(f"{num1} / {num2} = {result}")
                is_first = False
            else:
                print(f"{result2} / {num2} = {result}")

        next_or_not = input(
            f'Type "y" to continue calculation with {result}, or type "n" to start a new calculation: ')
        if next_or_not == "y":
            continue
        elif next_or_not == "n":
            break
    else:
        print("Invalid input")


# calculate_program()

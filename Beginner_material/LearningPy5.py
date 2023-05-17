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

range1 = int(input("Input the first range: "))
range2 = int(input("Input the second range: "))

for number in range(range1, range2):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

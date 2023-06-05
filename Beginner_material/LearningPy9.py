# PYTHON DICTIONARIES
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           }

# Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# Create an empty dictionary
# empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Grading Program ===========================

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]

#     if score > 91:
#         student_grades[student] = "Outstanding"
#     elif score > 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# Nesting Lists and Dictionaries

# Nesting Dictionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities": ["Paris", "Lille", "Dijon"],
#         "visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities": ["Hamburg", "Berlin", "Stuttgart"],
#         "visits": 15
#     }
# ]


# def add_new_country(country_visited, time_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = time_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)


# add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
# print(travel_log)


# Blind Auction Program ========================

from blind_auction.BidLogo import logo
import os
def cls(): return os.system('cls')


def blind_auction():
    bid_data = []
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    while True:
        data_input = {}
        name_input = input("What's your name? ")
        bid_input = input("What's your bid? $")
        data_input["name"] = name_input
        data_input["bid_input"] = bid_input
        bid_data.append(data_input)
        ask_option = input("Are there any other bidders? (y/n) ")
        if ask_option == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            max_bid = 0
            bidder_name = ""
            for key in bid_data:
                bid = int(key["bid_input"])
                if bid > max_bid:
                    max_bid = bid
                    bidder_name = key["name"]

            print(f"The winner this bidding is {bidder_name} with ${max_bid}")
            break


blind_auction()

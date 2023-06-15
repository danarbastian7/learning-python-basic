# COFFEE MACHINE PROJECT

# Coin:
# Penny = 0.01
# Dime = 0.1
# Nickle = 0.05
# Quarter = 0.25
from coffemachine_support.data import MENU, resources
from coffemachine_support.coffemachine import money_check, money_count, val_choose, subtract_ingredients


order = True
total_income = 0
while order:
    total_res = resources

    user_input = int(input(
        f"What would you like?\n1. Espresso ${MENU['espresso']['cost']}\n2. Latte ${MENU['latte']['cost']}\n3. Cappuccino ${MENU['cappuccino']['cost']}\nType 1/2/3: "))
    user_choice = val_choose(user_input)
    if 1 <= user_input <= 3:
        user_choose = MENU[user_choice]
    elif user_input == 4:
        print(
            f"{user_choice}\nMilk: {total_res['milk']}ml\nWater: {total_res['water']}ml\nCoffee: {total_res['coffee']}ml\nMoney Income: $ {total_income}\n")
        continue
    else:
        user_choice
        continue

    quarter = int(input("How many quarter?: "))
    nickle = int(input("How many nickles?: "))
    dime = int(input("How many dimes?: "))
    penny = int(input("How many pennies?: "))
    total = money_count(quarter, nickle, dime, penny)
    checking = money_check(total, user_choose['cost'])

    if checking != False:
        total_res = subtract_ingredients(
            user_choose['ingredients'], resources)

        if total_res == None:
            print("I'am sorry, we don't have enough resource.\nWe will back soon!")
            break

        else:
            print(
                f"\nYou pay with ${total}\nHere your coffee ☕️\nHere your change ${round(checking,2)}\n")
            total_income += user_choose['cost']

    else:
        print(
            f"Sorry not enough money, your money ${round(total,2)} will be refunded\n")

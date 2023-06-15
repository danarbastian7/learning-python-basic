def money_count(a, b, c, d):
    return (a * 0.25) + (b * 0.05) + (c * 0.1) + (d * 0.01)


def money_check(a, b):
    if a >= b:
        return a-b
    elif a < b:
        return False


def val_choose(a):
    if 1 <= a <= 4:
        if a == 1:
            return "espresso"
        elif a == 2:
            return "latte"
        elif a == 3:
            return "cappuccino"
        else:
            return "Report"

    else:
        print("Invalid input. Please type 1/2/3\n")


def subtract_ingredients(ingredients, resources):
    for ingredient, amount in ingredients.items():
        if ingredient in resources:
            if resources[ingredient] >= amount:
                resources[ingredient] -= amount
            else:
                return None
        else:
            return None

    return resources

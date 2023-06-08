def guess(lvl):
    if lvl == 1:
        return 10

    elif lvl == 2:
        return 7

    elif lvl == 3:
        return 5


def guess_remain(guess):
    guess -= 1
    return guess


def asking_user():

    try_answer = int(input("Make a guess: "))
    return try_answer


def ask_to_play_again():
    play_again = input("Do you want to play again? (y/n)\n")
    if play_again == "y":
        return True
    elif play_again == "n":
        return False
    else:
        while True:
            play_again = input("Invalid input. Please enter 'y' or 'n'.\n")
            if play_again == "y":
                return True
            elif play_again == "n":
                return False


def search_dif(x, y):
    if x > y and 0 < x-y <= 5:
        return "A little lower to get win!\nGuess again."
    elif x > y and 0 < x-y <= 10:
        return "Your answer is little high! Lower please.\nGuess again."
    elif x > y and x-y > 10:
        return "Your answer is too High!\nGuess again."
    elif x < y and 0 > x-y >= -3:
        return "A little higher answer please.\nGuess again."
    elif x < y and -3 >= x-y >= -10:
        return "Make higher answer please!\nGuess again."
    elif x < y and -10 > x-y:
        return "Your answer is too low. Higher please!\nGuess again."

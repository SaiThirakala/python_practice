import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The String that the user will see, when
        they are prompted to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Invalid input: {}".format(temp))


print(input.__doc__)
print("-" * 80)
print(get_integer.__doc__)
print("-" * 80)

highest = 10
answer = random.randint(1, highest)
# TODO: Remove after testing
print(answer)

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it")
#     else:
#         print("Sorry, guessed incorrectly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it")
#     else:
#         print("Sorry, guessed incorrectly")
# else:
#     print("You got it first time")

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it")
#     else:
#         print("Sorry, guessed incorrectly")
# else:
#     print("You got it first time")

game_state = True
guess_trys = 1
guess = get_integer("Please guess a number between 1 and {}".format(highest))

while game_state:
    if guess == 0:
        print("Game had quit")
        break
    elif guess != answer:
        guess_trys += 1
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guess = get_integer(": ")
    else:
        print("You got it in {0} tries".format(guess_trys))
        game_state = False

import random

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
guess = int(input("Please guess a number between 1 and {}".format(highest)))

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
        guess = int(input())
    else:
        print("You got it in {0} tries".format(guess_trys))
        game_state = False

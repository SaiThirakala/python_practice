# day = "Monday"
# temperature = 30
# raining = True
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go swimming")
# else:
#     print("Learn Python")

# code is unreachable since 0 cant be evaluated to a boolean
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name")
if name != "":
    print("Hello, {0}".format(name))
else:
    print("No name?")

parrot = "Norwegian Blue"
letter = input("Enter a char: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont need that letter")

activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

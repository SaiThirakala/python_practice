cuisines = ["Mexican", "Chinese", "Indian", "Korean"]

print("Please choose an option from the list below"
      "Enter the corresponding number: ")
for i in cuisines:
    print("{}. {}".format(cuisines.index(i) + 1, i))

option = int(input())
while option != 0:
    if option < 1 or option > len(cuisines):
        print("You must choose a valid option!")
    else:
        print("You chose {} food!".format(cuisines[option - 1]))
    option = int(input())

print("You are done choosing!")
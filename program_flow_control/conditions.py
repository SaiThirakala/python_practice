age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
#     print("Have a good day at work")

if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 40)

if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("Have a good day at work")

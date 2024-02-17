available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "mouse mat",
    "6": "hdmi cable",
    "7": "dvd drive",
}

current_choice = None
computer_parts = {}  # create an empty dictionary

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # Remove item if already in shopping cart
            print(f'Removing {chosen_part}')
            computer_parts.pop(current_choice)
        else:
            # Add item if not already in shopping cart
            print(f'Adding {chosen_part}')
            computer_parts[current_choice] = chosen_part
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f'{key}: {value}')
        print("0: to quit")

    current_choice = input("> ")
else:
    print(f'Shopping cart: {computer_parts}')
from dict_and_set.dict.contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add an item and its corresponding amount to a dictionary.
    If an item is already in the dictionary, just add the amount.
    :param data: The dictionary being added to.
    :param item: The item being added to the dictionary.
    :param amount: The value for the item in the dictionary.
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


print(pantry)
print(recipes)

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

# Shopping list
ingredients_needed = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 25)
    for key, value in display_dict.items():
        print(f'{key} - {value}')

    choice = input(": ")

    if choice == '0':
        break
    elif choice in display_dict:
        # Selecting a meal
        selected_item = display_dict[choice]
        print(f'You have selected {selected_item}')

        # Get ingredients of selected meal and print them
        print("Checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)

        # Checking for ingredients necessary to make a meal
        # Checks how much of ingredient is required and prints how
        # much more of ingredient is needed
        for item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f'\t{item} OK')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f'\tYou need {quantity_to_buy} more of {item}')
                # Add missing ingredients to a shopping list
                add_shopping_item(ingredients_needed, item, quantity_to_buy)


print(f'Shopping List: {ingredients_needed}')





import copy

animals = {
    'lion': ['scary', 'big', 'cat'],
    'elephant': ['big', 'grey', 'wrinkled'],
    'teddy': ['cuddly', 'stuffed'],
}

# Perform a shallow copy
# things = animals.copy()

# animals['teddy'] = 'toy'

# Perform a deep copy
things = copy.deepcopy(animals)
print(id(animals['teddy']), animals['teddy'])
print(id(things['teddy']), things['teddy'])

print()

things['teddy'].append("toy")
print(animals['teddy'])
print(things['teddy'])


def deep_copy(dictionary: dict) -> dict:
    """
    Copy a deep copy of a dictionary. Also create deep
    copies of `list` or `dict` values.

    Function will produce AttributeError if values are not lists or
    dictionaries.
    :param dictionary: The dictionary to copy.
    :return: The deep copy of the dictionary.
    """
    new_dict = {}
    for key, value in dictionary.items():
        new_list = []
        for item in value:
            new_list.append(item)
        new_dict[key] = new_list

    return new_dict


things2 = deep_copy(animals)
print(id(animals['teddy']))
print((id(things2['teddy'])))

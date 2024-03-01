filename = 'country_info.txt'


def file_to_dict(input_filename: str) -> dict:
    """
    Read a txt file of country information and create a dictionary
    of countries and their associated characteristics.

    :param input_filename: The name of the file to read over.
    :return: The dictionary of countries and their associated
    characteristics.
    """
    countries_dict = {}
    with open(input_filename) as country_file:
        country_file.readline()
        for row in country_file:
            data = row.strip('\n').split('|')
            country, capital, code, code3, dialing, timezone, currency = data
            # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
            country_dict = {
                'name': country,
                'capital': capital,
                'country_code': code,
                'cc3': code3,
                'dialing_code': dialing,
                'timezone': timezone,
                'currency': currency,
            }
            countries_dict[country.casefold()] = country_dict

    return countries_dict


countries = file_to_dict(filename)
print(countries)


def get_blank_vals(countries_dict: dict, *params: str) -> list:
    """
    Iterate through a dictionary of dictionaries. If the value dictionary
    has any blank "" parameters, add the key of that value to a list. Return
    the list of all keys that have blank parameters in its value dict.

    :param countries_dict: The dictionary being iterated over.
    :param params: The keys in the value dictionary that are being checked if their
    values are blank.
    :return: The list of keys that have value dictionaries that contain blank
    values.
    """
    blank_set = set()
    for param in params:
        for name, country_values in countries_dict.items():
            if "" == country_values[param]:
                blank_set.add(name)

    return list(blank_set)


def get_capital(countries_dict: dict) -> None:
    """
    Get the capital of a country using the country's name.

    :param countries_dict: The dictionary of all countries and associated
    characteristics.
    """
    no_capitals = get_blank_vals(countries_dict, 'capital')
    while True:
        country_name = input("Enter the country name: ")
        if country_name in countries_dict:
            if country_name in no_capitals:
                print("This country does not have a capital!!")
            else:
                print(countries_dict[country_name]['capital'])
        elif country_name == 'done':
            break


get_capital(countries)


def get_blanks(countries_dict: dict) -> list:
    blank_list = []
    for name, country_values in countries_dict.items():
        if "" in list(country_values.values()):
            blank_list.append(name)

    return blank_list

# print(get_blank_vals(countries, 'capital'))

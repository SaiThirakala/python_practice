vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triump Street Triple',
}

# my_car = vehicles['fiesta']
# # Indexing incorrect string causes an KeyError
# # wrong_index = vehicles['Fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get('er5')
# print(learner)
# # Passing incorrect string for 'get' return None
# wrong_get = vehicles.get("ER5")
# print(wrong_get)

# Iterating over a dictionary, not efficient
# for key in vehicles:
#     print(key, vehicles[key], sep=": ")

# Adding key/value pairs to dictionary
vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjet'] = "Bombardier Learjet 75"
vehicles['toy'] = 'glider'

# Changing a value in a dictionary
vehicles['virago'] = 'Yamaha XV535'

# Deleting items from a dictionary
del vehicles['starfighter']
# del vehicles['f1']
result = vehicles.pop('f1', None)
print(result)
plane = vehicles.pop('learjet')
print(plane)

bike = vehicles.pop('tenere', 'not present')
print()

# More efficient way to iterate over a dictionary
for key, value in vehicles.items():
    print(key, value, sep=": ")

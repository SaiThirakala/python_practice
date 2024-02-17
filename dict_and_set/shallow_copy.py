animals = {
    'lion': 'scary',
    'elephant': 'big',
    'teddy': 'cuddly',
}

things = animals.copy()
animals['teddy'] = 'toy'
print(animals['teddy'])
print(things['teddy'])
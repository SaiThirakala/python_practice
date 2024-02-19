animals = {
    'turtle',
    'horse',
    'robin',
    'python',
    'swallow',
    'hedgehog',
    'wren',
    'aardvark',
    'cat',
}

birds = {
    'robin',
    'swallow',
    'wren',
}

print(f'birds is s subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(f'birds is a superset of animals: {birds.issuperset(animals)}')
print(birds <= animals)
print(birds < animals)

print("*" * 50)
garden_birds = {
    'robin',
    'swallow',
    'wren',
}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print("*" * 50)
more_birds = {
    'robin',
    'swallow',
    'wren',
}
print(garden_birds >= more_birds)


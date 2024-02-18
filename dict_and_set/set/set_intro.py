farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()
print("indexing a sequence")
animals_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animals_list[3]
print(goat)

print("indexing a set is not possible")

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
# Sets that contain the same items are considered equal
if more_animals == farm_animals:
    print("sets are equal")
else:
    print('sets are different')

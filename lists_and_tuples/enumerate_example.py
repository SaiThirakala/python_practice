# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for i in enumerate("abcdefh"):
    index, character = i
    print(index, character)


index, character = (0, 'a')
print(index)
print(character)
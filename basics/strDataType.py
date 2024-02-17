parrot = "Norwegian Blue"
print(parrot)
# print char at index 3 in string parrot
print(parrot[3])

# Mini challenge: print out "we win" where each char is at a new line
word = 'we win'
for i in range(0, len(word)):
    print(word[i])

# Print 'we win' from 'Norwegian Blue" using negative indexing
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# Slicing a string
# Norweg
print(parrot[0:6])
# we
print(parrot[3:5])
# Blue
print(parrot[10:])
# Norweg
print(parrot[:6])
# ian Blue
print(parrot[6:])
# Norwegian Blue
print(parrot[:6] + parrot[6:])
print(parrot[:])

# Slicing with negative numbers
print(parrot[-4:-2]) # Bl
print(parrot[-4: 12]) # Bl

# Slicing with steps
# parrot[0:6:2]
# slice starts at index 0, up to 6 exclusive, and in steps of 2
# Nre
print(parrot[0:6:2])
#NreinBu
print(parrot[0::2])

# Slicing with steps backwards
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(letters[::-1])

#qpo
print(letters[16:13:-1])
#edcba
print(letters[4::-1])
#last 8 chars in reverse order
print(letters[25:17:-1])
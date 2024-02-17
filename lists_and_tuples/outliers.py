data = [4, 5, 104, 105, 110, 120, 130, 1,
        50, 160, 170, 183, 185, 187, 188,
        191, 350, 360]
# delete first 3 values
# del data[0:2]
# print(data)
#
# del data[16:]
# print(data)
min_valid = 100
max_valid = 200

# length of list changes, so not all values are deleted correctly
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#         index -= 1
#
# print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop) # for debugging
del data[:stop]
print(data)


# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break

print(start)
del data[start:]
print(data)
small_ints = set(range(21))
print(small_ints)

# Clearing all items from a set
# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

# Discarding an item that does not exists doesnt change anything
small_ints.discard(99)
print(small_ints)


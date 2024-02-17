# prints numbers from 1 to 20
for i in range(1, 21):
    print("i is now {0}".format(i))

print("-" * 20)

# prints number from 0 to 9
for i in range(10):
    print("i is now {0}".format(i))

print("-" * 20)

# step through ranges in 2s
# 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)

# step through ranges backwards
# 10, 8, 6, 4, 2
for i in range(10, 0, -2):
    print(i)


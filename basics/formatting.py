# add colon after replacement field to specify width
# lines up numbers
for i in range(1, 13):
    print("no. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print()

# add < in front of width to align numbers to the left
# add ^ to center
for i in range(1, 13):
    print("no. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))

print()

# general format defaults to printing 15 decimal values
print("Pi is approximately {0:12}".format(22 / 7))
# formats decimal to 6 decimal places within field width of 12
print("Pi is approximately {0:12f}".format(22 / 7))
# decimal precision of 50 prioritized over field width of 12
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
# left aligned
print("Pi is approximately {0:<72.50f}".format(22 / 7))




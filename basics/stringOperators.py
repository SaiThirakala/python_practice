# Python 3 has five sequence types built in
# string
# list
# tuple
# range
# bytes and bytearray

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thurs" in today) # False

# concat an int to a string
age = 24
print("M y age is " + str(age) + " years")

# using format
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {1}, Feb: {0}, Apr: {2}". format(28, 31, 30))

print("""
Jan: {1}
Feb: {0}
Apr: {2}
""".format(28, 31, 30))
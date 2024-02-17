shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"]
another_list = shopping_list

# Lists ids are the same
print(id(shopping_list))
print(id(another_list))

# Add an item in the list
shopping_list += ["cookies"]

# Id of shopping_list doesn't change
# even though list has changed
print(shopping_list)
print(id(shopping_list))

# another_list reflects changes made to shopping_list
# only 1 list exists, but has multiple names referencing it
print(another_list)

# a, b, c, d, e, f all refer to the same list
a = b = c = d = e = f = another_list

print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)
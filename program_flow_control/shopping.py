shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# # loop will skip over "spam" item
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("Buy " + item)

# # loop will stop when it encounters "spam" item
# for item in shopping_list:
#     if item == "spam":
#         break
#     print("Buy " + item)

# finding an item in a list
item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
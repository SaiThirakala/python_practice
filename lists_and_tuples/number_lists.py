empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# a sorted list will contain items of the same type as original list
digits = sorted("432985617")
print(digits)

# ways to copy a list
more_numbers = list(numbers)
more_numbers_2 = numbers[:]
more_numbers_3 = numbers.copy()
print(more_numbers)

# lists contain same items, but are not the same list
# lists themselves are different
print(numbers is more_numbers)
# lists contain the same items
print(numbers == more_numbers)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("is"))

# even.extend(odd)
# print(even)
#
# even.sort()
# print(even)
#
# even.sort(reverse=True)
# print(even)
panagram = ("The quick brown "
            "fox jumps\tover "
            "the lazy dog")

words = panagram.split()
print(words)

numbers = "9,223,372,036,283,291,202"
print(numbers.split(","))

nums = input("Please enter three numbers: ")
nums_split = nums.split(",")
print(int(nums_split[0]) + int(nums_split[1]) - int(nums_split[2]))
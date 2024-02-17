def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    :param x: The first number to multiply.
    :param y: The second number to multiply.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check is a string is a palindrome: the same string
    that reads the same forwards or backwards.

    :param string: The String that is being checked is it
        is a palindrome.
    :return: True if the `string` is a palindrome, False is
        it is not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check is a sentence is a palindrome.

    The function ignores whitespace, capitalization and punctuation
    in the sentence.
    :param sentence: The sentence to be checked.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    # print(string)
    return is_palindrome(string)


# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

# word = input("Enter a sentence to check")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

def fizz_buzz(number: int) -> str:
    """
    Return the str `fizz` if `number` is divisible by 3 or
    `buzz` if divisible by 5. If `number` is divisible by both
    3 and 5, return `fizz buzz`.
    :param number: The integer being checked.
    :return: The string `fizz` or `buzz` or `fizz buzz`.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


print("Play Fizz Buzz!\nIf the number is divisible by 3, type 'fizz'.\n"
      "If it's divisible by 5, type 'buzz'.\nIf its divisible by both, "
      "type 'fizz buzz'")

count = 1
while count < 100:
    print(f'{count}: {fizz_buzz(count)}')
    count += 1
    answer = input("Your turn: {}".format(count))

    if answer != fizz_buzz(count):
        print("YOU LOSE!!")
        break

    count += 1
else:
    print("YOU WIN!!")


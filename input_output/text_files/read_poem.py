# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.strip(), end="")
#     print(len(line))
#
# jabber.close()
#
# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line, end="")
#     lines = jabber.readlines()
#
# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end="")  # Processing file in reverse order
#
# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()
#
# for character in reversed(text):
#     print(character, end="")

with open("Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break

    

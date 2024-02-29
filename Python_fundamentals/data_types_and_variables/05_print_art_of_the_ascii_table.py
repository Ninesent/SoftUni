first_character = int(input())
second_character = int(input())

for number in range(first_character, second_character + 1):
    print(chr(number), end = " ")
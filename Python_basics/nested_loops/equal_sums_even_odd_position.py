number_one = int(input())
number_two = int(input())



for number in range(number_one, number_two + 1):
    number_to_str = str(number)
    odd_number = 0
    even_number = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            odd_number += int(digit)
        else:
            even_number += int(digit)

    if even_number == odd_number:
        print(number, end=" ")



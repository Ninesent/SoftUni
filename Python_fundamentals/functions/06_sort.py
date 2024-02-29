def sort_number(number: list) -> list:
    number_as_integer_list = []
    for number in number:
        number_as_integer_list.append(int(number))
    number_as_integer_list.sort()
    return number_as_integer_list


numbers = input().split()

print(sort_number(numbers))

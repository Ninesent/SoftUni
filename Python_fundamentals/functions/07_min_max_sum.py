result_list = []


def min_max_sum(number_list: list) -> int:
    number_as_int = []
    for number in number_list:
        number_as_int.append(int(number))

    result_list.append(f"The minimum number is {min(number_as_int)}")
    result_list.append(f"The maximum number is {max(number_as_int)}")
    result_list.append(f"The sum number is: {sum(number_as_int)}")

    return result_list


numbers = input().split()
min_max_sum(numbers)
print(*result_list, sep="\n")

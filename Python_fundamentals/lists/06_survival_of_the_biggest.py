numbers_as_string = input().split()
remove_number_count = int(input())
numbers_as_integer = []

for number_conversion in numbers_as_string:
    numbers_as_integer.append(int(number_conversion))

sorted_list_of_integers = numbers_as_integer.copy()
sorted_list_of_integers.sort()
old_value = sorted_list_of_integers[0]
remove_counter = 0

for current_number_removal in sorted_list_of_integers:
    if current_number_removal > old_value:
        numbers_as_integer.remove(old_value)
        if old_value in numbers_as_integer:
            numbers_as_integer.remove(old_value)
            remove_counter += 1
        remove_counter += 1
        if remove_counter >= remove_number_count:
            break
    old_value = current_number_removal




print(*numbers_as_integer, sep = ", ")
number_count = int(input())

left_side = 0
right_side = 0

for numbers in range(number_count):
    current_number = int(input())
    if numbers < number_count:
        left_side += current_number
    else:
        right_side += current_number

sum = left_side + right_side
print(sum)
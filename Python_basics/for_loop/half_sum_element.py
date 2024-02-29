import sys

numbers = int(input())

max_number = -sys.maxsize
sum_numbers = 0

for n in range(numbers):
    current_number = int(input())
    if max_number < current_number:
       max_number = current_number

    sum_numbers += current_number

final_sum = sum_numbers - max_number

if final_sum == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - final_sum)}")

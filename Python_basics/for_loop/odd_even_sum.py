number_count = int(input())

even_side = 0
odd_side = 0

for numbers in range(number_count):
    current_number = int(input())
    if numbers % 2 == 0:
        even_side += current_number
    else:
        odd_side += current_number

if even_side == odd_side:
    print("Yes")
    print(f"Sum = {even_side}")
else:
    difference = abs(even_side - odd_side)
    print("No")
    print(f"Diff = {difference}")
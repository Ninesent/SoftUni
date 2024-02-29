number= int(input())

for num in range(1111, 10_000):
    num_as_str = str(num)

    is_special = True

    for _, digit in enumerate(num_as_str):
        current_digit = int(digit)

        if current_digit == 0:
            is_special = False
            break

        if not number % current_digit == 0:
            is_special = False
            break

    if is_special:
        print(f"{num}", end=" ")


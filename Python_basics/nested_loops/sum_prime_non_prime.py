command = input()
prime_sum = 0
non_prime_sum = 0

while command != "stop":
    command_to_int = int(command)
    if command_to_int < 0:
        command_to_int = 0
        print("Number is negative.")


    for i in range(2, command_to_int):
        if command_to_int % i == 0:
            non_prime_sum += command_to_int
            break
    else:
        prime_sum += command_to_int

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")

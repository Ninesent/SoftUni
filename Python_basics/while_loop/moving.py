width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

left_space = total_space

command = input()

while not command == "Done":
    current_box = int(command)
    left_space -= current_box
    if left_space <= 0:
        break

    command = input()

if command == "Done":
    print(f"{left_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(left_space)} Cubic meters more.")

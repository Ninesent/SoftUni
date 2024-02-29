import sys

min_number = sys.maxsize
command = input()

while command != "Stop":
    current_command = int(command)
    if current_command < min_number:
        min_number = current_command

    command = input()

print(min_number)
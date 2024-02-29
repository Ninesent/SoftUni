import sys

max_number = - sys.maxsize
command = input()

while command != "Stop":
    current_command = int(command)
    if current_command > max_number:
        max_number = current_command

    command = input()

print(max_number)
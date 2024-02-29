def translate(string_to_change, char, replacement):
    while char in string_to_change:
        string_to_change = string_to_change.replace(char, replacement)

    return string_to_change


def includes(string_to_change, substring):
    if substring in string_to_change:
        print("True")
    else:
        print("False")


def lowercase(string_to_manipulate):
    string_to_manipulate = string_to_manipulate.lower()
    return string_to_manipulate


def find_index(string_to_check, letter):
    if letter in string_to_check:
        result = string_to_check.rindex(letter)
        print(result)


def remove_index(string_to_manipulate, start_index, end_index):
    end_index += start_index
    if start_index in range(len(string_to_manipulate)) and end_index in range(len(string_to_manipulate)):
        string_to_manipulate = string_to_manipulate[:start_index] + string_to_manipulate[end_index:]
        return string_to_manipulate


string_to_manipulate = input()
command = input()

while command != "End":

    command = command.split()

    if command[0] == "Translate":
        char, replacement = command[1], command[2]
        string_to_manipulate = translate(string_to_manipulate, char, replacement)
        print(string_to_manipulate)

    elif command[0] == "Includes":
        substring = command[1]
        includes(string_to_manipulate, substring)

    elif command[0] == "Start":
        substring = str(command[1])
        print(string_to_manipulate.startswith(substring))


    elif command[0] == "Lowercase":
        string_to_manipulate = lowercase(string_to_manipulate)
        print(string_to_manipulate)

    elif command[0] == "FindIndex":
        letter = command[1]
        find_index(string_to_manipulate, letter)

    elif command[0] == "Remove":
        start_index, end_index = int(command[1]), int(command[2])
        string_to_manipulate = remove_index(string_to_manipulate, start_index, end_index)
        print(string_to_manipulate)

    command = input()

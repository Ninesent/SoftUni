import re

pattern = r"(\|)([A-Z]{4,})(\1)(:)(#)([A-Za-z]+)\s{1}([A-Za-z]+)(\5)"


number_of_inputs = int(input())

for input_to_check in range(number_of_inputs):
    boss_to_check = input()

    match = re.findall(pattern, boss_to_check)
# [('|', 'PETER', '|', ':', '#', 'Lead', 'architect', '#')]
    if match:
        for element in match:
            print(f"{element[1]}, The {element[5]} {element[6]}")
            print(f">> Strength: {len(element[1])}")
            title = "".join(element[0])
            armor = len(element[5]) + len(element[6]) + 1
            print(f">> Armor: {armor} ")
    else:
        print("Access denied!")
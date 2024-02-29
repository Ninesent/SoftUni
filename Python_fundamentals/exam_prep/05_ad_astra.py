import re

information = input()

pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d{0,10000})(\1)"

matches = re.findall(pattern, information)

total_calories = sum([int(match[5]) for match in matches])

calories_per_day = total_calories // 2000
print(f"You have food to last you for: {calories_per_day} days!")

for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

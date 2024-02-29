days = int(input())
type = input()
score = input()

room = 18
apartment = 25
president_apartment = 35.00

sum = 0

if type == "room for one person":
    room = 18
    new_type = room
    sum = (days - 1) * new_type
elif type == "apartment":
    new_type = apartment
    sum = (days - 1) * new_type
    if days < 10:
        sum *= 0.70
    elif 10 < days <= 15:
        sum *= 0.65
    elif days > 15:
        sum *= 0.50
elif type == "president apartment":
    new_type = president_apartment
    sum = (days - 1) * new_type
    if days < 10:
        sum *= 0.90
    elif 10 < days <= 15:
        sum *= 0.85
    elif days > 15:
        sum *= 0.80


if score == "positive":
    sum *= 1.25
elif score == "negative":
    sum *= 0.90

print(f"{sum :.2f}")



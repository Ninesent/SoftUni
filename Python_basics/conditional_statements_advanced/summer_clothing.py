celsius = int(input())
time_of_the_day = input()

outfit = 0
shoes = 0

if time_of_the_day == "Morning":
    if 10 <= celsius <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < celsius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
if time_of_the_day == "Afternoon":
    if 10 <= celsius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < celsius <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif celsius >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
if time_of_the_day == "Evening":
    if 10 <= celsius <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < celsius <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif celsius >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {celsius} degrees, get your {outfit} and {shoes}.")
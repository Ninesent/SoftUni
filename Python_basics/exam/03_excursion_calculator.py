people_amount = int(input())
season = input()
price_per_person = 0

if people_amount > 5:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85
elif people_amount <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86

total_cost = people_amount * price_per_person

if season == "summer":
    total_cost *= 0.85
elif season == "winter":
    total_cost *= 1.08

print(f"{total_cost:.2f} leva.")

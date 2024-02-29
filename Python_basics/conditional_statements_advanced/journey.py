budget = float(input())
season = input()

type = 0
destination = 0
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type = "Camp"
        budget *= 0.30
    elif season == "winter":
        type = "Hotel"
        budget *= 0.70
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        budget *= 0.40
    elif season == "winter":
        type = "Hotel"
        budget *= 0.80
if budget > 1000:
    type = "Hotel"
    destination = "Europe"
    budget *= 0.90



print(f"Somewhere in {destination}")
print(f"{type} - {budget :.2f}")
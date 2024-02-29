budget = int(input())
season = input()
fishermen_amount = int(input())

boat_cost = 0
discount = 0
extra_discount = 0

if season == "Spring":
    boat_cost = 3000
elif season == "Summer" or season == "Autumn":
    boat_cost = 4200
elif season == "Winter":
    boat_cost = 2600

if fishermen_amount <= 6:
    discount = 0.10
elif fishermen_amount <= 11:
    discount = 0.15
else:
    discount = 0.25

if fishermen_amount % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_cost = boat_cost * (1 - discount) * (1 - extra_discount)

if budget >= total_cost:
    print(f"Yes! You have {budget - total_cost :.2f} leva left.")
else:
    print(f"Not enough money! You need {total_cost - budget :.2f} leva.")
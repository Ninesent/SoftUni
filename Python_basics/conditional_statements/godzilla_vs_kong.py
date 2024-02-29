movie_budget = float(input())
number_of_extras = int(input())
clothing_price_extras = float(input())

EXTRAS_DISCOUNT = 0.10
DECOR_PERCANTAGE = 0.10

decor = movie_budget * DECOR_PERCANTAGE

extras_sum = number_of_extras * clothing_price_extras

if number_of_extras >= 150:
    extras_discount = extras_sum * EXTRAS_DISCOUNT
    extras_sum -= extras_discount

decor_and_extras = decor + extras_sum



if decor_and_extras > movie_budget:
    print(f"Not enough money!\nWingard needs {decor_and_extras - movie_budget:.2f} leva more.")
else:
    print(f"Action!\nWingard starts filming with {movie_budget - decor_and_extras:.2f} leva left.")





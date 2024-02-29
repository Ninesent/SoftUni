month = input() # May, June, July, August, September или October;
nights = int(input())


discount = 0
studio_price_per_night = 0
apartment_price_per_night = 0

if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 14 > nights > 7:
        studio_price_per_night *= 0.95
    elif nights > 14:
        studio_price_per_night *= 0.70
elif month == "September" or month == "June":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights > 14:
        studio_price_per_night *= 0.80
elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights > 14:
    apartment_price_per_night *= 0.90

apartment_total_cost = nights * apartment_price_per_night
studio_total_cost = nights * studio_price_per_night

print(f"Apartment: {apartment_total_cost:.2f} lv.")
print(f"Studio: {studio_total_cost:.2f} lv.")

from math import ceil

missing_days = int(input())
food_left_in_kg = int(input())
food_for_first_deer = float(input())
food_for_second_deer = float(input())
food_for_third_deer = float(input())

total_food_consumed = (missing_days * food_for_first_deer) + (missing_days * food_for_second_deer) + \
                      (missing_days * food_for_third_deer)

total_food_left = abs(food_left_in_kg - total_food_consumed)

if food_left_in_kg >= total_food_consumed:
    print(f"{int(total_food_left)} kilos of food left.")
else:
    print(f"{ceil(total_food_left)} more kilos of food are needed.")
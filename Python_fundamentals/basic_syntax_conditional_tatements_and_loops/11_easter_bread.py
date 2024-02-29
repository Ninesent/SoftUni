budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

total_cost = flour_price + eggs_price + (milk_price * 0.25)
colored_eggs_counter = 0
current_bread = 0

while budget > 0:
    if total_cost >= budget:
        break
    colored_eggs_counter += 3
    current_bread += 1
    if current_bread % 3 == 0:
        eggs_lost = current_bread - 2
        if eggs_lost > colored_eggs_counter:
            break
        colored_eggs_counter -= eggs_lost

    budget -= total_cost




print(f"You made {current_bread} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
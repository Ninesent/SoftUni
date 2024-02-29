trip_cost = float(input())
available_money = float(input())
spend_counter = 0
days = 0

total_money = available_money

while True:
    action = input()
    current_amount = float(input())
    days += 1

    if action == "save":
        total_money += current_amount
        spend_counter = 0
        if total_money >= trip_cost:
            break


    elif action == "spend":
        spend_counter += 1
        total_money -= current_amount
        if total_money < 0:
            total_money = 0

    if spend_counter >= 5:
        break

if total_money >= trip_cost:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(days)
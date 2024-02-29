change_amount = float(input())

pennies = int(change_amount * 100)

coins_amount = 0

while pennies > 0:
    if pennies > 200:
        pennies -= 200
        coins_amount += 1
    elif pennies >= 100:
        pennies -= 100
        coins_amount += 1
    elif pennies >= 50:
        pennies -= 50
        coins_amount += 1
    elif pennies >= 20:
        pennies -= 20
        coins_amount += 1
    elif pennies >= 10:
        pennies -= 10
        coins_amount += 1
    elif pennies >= 5:
        pennies -= 5
        coins_amount += 1
    elif pennies >= 2:
        pennies -= 2
        coins_amount += 1
    elif pennies >= 1:
        pennies -= 1
        coins_amount += 1

print(coins_amount)
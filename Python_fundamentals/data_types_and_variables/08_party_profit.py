companion_size = int(input())
days = int(input())

coins_per_person = 0
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companion_size -= 2
    if current_day % 15 == 0:
        companion_size += 5
    if current_day % 3 == 0:
        coins -= companion_size * 3
    if current_day % 5 == 0:
        coins += companion_size * 20
        if current_day % 3 == 0:
            coins -= companion_size * 2
    coins += 50
    coins -= companion_size * 2
    coins_per_person = int(coins // companion_size)

print(f"{companion_size} companions received {coins_per_person} coins each.")
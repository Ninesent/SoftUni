flower_type = input()
flower_amount = int(input())
budget = int(input())

rose_price = 5.00
dahlias_price = 3.80
tulip_price = 2.80
narcissus_price = 3.00
gladiolus_price = 2.50

price = 0
discount = 0

if flower_type == "Roses":
    price = rose_price
    if flower_amount > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = dahlias_price
    if flower_amount > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = tulip_price
    if flower_amount > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = narcissus_price
    if flower_amount < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    price = gladiolus_price
    if flower_amount < 80:
        discount = -0.20

total_price = flower_amount * price * (1 - discount)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} "
          f"and {budget - total_price :.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget :.2f} leva more.")

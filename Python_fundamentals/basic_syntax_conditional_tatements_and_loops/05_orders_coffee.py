number_of_orders = int(input())
total_cost = 0

for coffees in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if price_per_capsule > 100 or days > 31 or capsules_needed > 2000:
        continue

    if price_per_capsule < 0.01 or days < 1 or capsules_needed < 1:
        continue

    cost_per_order = (capsules_needed * price_per_capsule) * days
    print(f"The price for the coffee is: ${cost_per_order:.2f}")
    total_cost += cost_per_order

print(f"Total: ${total_cost:.2f}")
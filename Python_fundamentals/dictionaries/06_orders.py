inventory = {}

while True:
    command = input()

    if command == "buy":
        break

    product_name, product_price, product_quantity = command.split()

    if not product_name in inventory.keys():
        inventory[product_name] = {}
        inventory[product_name]["quantity"] = 0

    inventory[product_name]["price"] = float(product_price)
    inventory[product_name]["quantity"] += int(product_quantity)

for item, price_and_quantity in inventory.items():
    total_price = price_and_quantity["price"] * price_and_quantity["quantity"]
    print(f"{item} -> {total_price:.2f}")





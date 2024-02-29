train_ticket = 150
items_for_sale = input().split("|")
starting_budget = float(input())
markup = 1.40
budget_left = starting_budget
new_item_price_list = []
profit = 0


for item in items_for_sale:
    item_split = item.split("->")
    item_type = item_split[0]
    item_price = float(item_split[1])

    if item_type == "Clothes" and item_price <= 50.00 and (budget_left - item_price >= 0):
        budget_left -= item_price
        new_item_price = item_price * markup
        new_item_price_list.append(new_item_price)
        profit += new_item_price - item_price
    elif item_type == "Shoes" and item_price <= 35.00 and (budget_left - item_price >= 0):
        budget_left -= item_price
        new_item_price = item_price * markup
        new_item_price_list.append(new_item_price)
        profit += new_item_price - item_price
    elif item_type == "Accessories" and item_price <= 20.50 and (budget_left - item_price >= 0):
        budget_left -= item_price
        new_item_price = item_price * markup
        new_item_price_list.append(new_item_price)
        profit += new_item_price - item_price

my_formatted_list = ["%.2f" % elem for elem in new_item_price_list]
print(*my_formatted_list)
print(f"Profit: {profit:.2f}")

if budget_left + sum(new_item_price_list) >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

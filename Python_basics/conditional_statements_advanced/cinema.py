project_type = input()
rows = int(input())
column = int(input())

income = 0
price = 0

if project_type == "Premiere":
    price = 12
elif project_type == "Normal":
    price = 7.50
elif project_type == "Discount":
    price = 5

income = price * (rows * column)

print(f"{income :.2f} leva")
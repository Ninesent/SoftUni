brewing_days = int(input())
total_rakia_amount = 0
rakia_calculation = 0
rakia_total_liters = 0

for _ in range(brewing_days):
    rakia_amount = float(input())
    current_celsius = float(input())
    rakia_total_liters += rakia_amount
    rakia_calculation = rakia_amount * current_celsius
    total_rakia_amount += rakia_calculation
    rakia_calculation = 0

average_celsius = total_rakia_amount / rakia_total_liters

print(f"Liter: {rakia_total_liters:.2f}")
print(f"Degrees: {average_celsius:.2f}")

if average_celsius < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_celsius < 42:
    print(f"Super!")
elif average_celsius >= 42:
    print(f"Dilution with distilled water!")

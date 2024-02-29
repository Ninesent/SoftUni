M2 = 7.61
DISCOUNT = 0.18

m2_worked_on = float(input())

discounted_sum = (m2_worked_on * M2) * DISCOUNT
total_sum = (m2_worked_on * M2) - discounted_sum

print(f"The final price is {total_sum} lv.")
print(f"The discount is: {discounted_sum} lv.")



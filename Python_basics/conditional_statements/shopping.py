GPU = 250
CPU = 0.35
RAM = 0.10
DISCOUNT = 0.15

total_sum = 0

budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = gpu_amount * GPU
cpu_price = gpu_price * CPU
ram_price = gpu_price * RAM

total_sum = gpu_price + (cpu_price * cpu_amount) + (ram_price * ram_amount)

if gpu_amount >= cpu_amount:
    discount = total_sum * DISCOUNT
    total_sum = total_sum - discount

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")




# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
#
# · Ако бюджета е достатъчен:
#
# "You have {остатъчен бюджет} leva left!"
#
# · Ако сумата надхвърля бюджета:
#
# "Not enough money! You need {нужна сума} leva more!"
deposit = input()
account_balance = 0


while not deposit == "NoMoreMoney":
    deposit_amount = float(deposit)
    if deposit_amount <= 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {deposit_amount:.2f}")
    account_balance += deposit_amount
    deposit = input()

print(f"Total: {account_balance:.2f}")

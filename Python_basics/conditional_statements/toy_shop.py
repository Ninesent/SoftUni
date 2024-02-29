PUZZLE = 2.60
TALKING_DOLL = 3
TEDDYBEAR = 4.10
MINION = 8.20
TRUCK = 2

PURCHASED_PRODCUTS_AMOUNT = 50
PURCHASED_PRODCUTS_BONUS = 0.25

STORE_RENT = 0.10


trip_cost = float(input())
puzzles_purchased = int(input())
talking_dolls_purchased = int(input())
teddybears_purchased = int(input())
minions_purchased = int(input())
trucks_purchased = int(input())

total_products_purchased = puzzles_purchased + talking_dolls_purchased + \
                           teddybears_purchased+ minions_purchased + trucks_purchased

total_price = (puzzles_purchased * PUZZLE) + (talking_dolls_purchased * TALKING_DOLL) + \
    (teddybears_purchased * TEDDYBEAR) + (minions_purchased * MINION) + (trucks_purchased * TRUCK)

if total_products_purchased >= PURCHASED_PRODCUTS_AMOUNT:
    new_total = total_price * (1 - PURCHASED_PRODCUTS_BONUS)
    rent = new_total *  STORE_RENT
    income = new_total - rent
else:
    rent = total_price * STORE_RENT
    income = total_price - rent



if income >= trip_cost:
    print(f"Yes! {income - trip_cost :.2f} lv left.")
else:
    print(f"Not enough money! {trip_cost - income :.2f} lv needed.")



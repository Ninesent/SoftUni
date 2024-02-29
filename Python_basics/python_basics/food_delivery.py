CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGAN_MENU = 8.15
DESERT = 0.20
DELIVERY_FEE = 2.50

chicken_menus = int(input())
fish_menus = int(input())
vegan_menu = int(input())

desert_fee = ((chicken_menus * CHICKEN_MENU) + (fish_menus * FISH_MENU) + (vegan_menu * VEGAN_MENU)) * DESERT
order_sum = (chicken_menus * CHICKEN_MENU) + (fish_menus * FISH_MENU) + (vegan_menu * VEGAN_MENU) + desert_fee \
            + DELIVERY_FEE

print(order_sum)


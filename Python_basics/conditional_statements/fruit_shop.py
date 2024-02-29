fruit = input()
day_of_the_week = input()
quantity = float(input())

banana = 2.50
apple = 1.20
orange = 0.85
grapefruit = 1.45
kiwi = 2.70
pineapple = 5.50
grapes = 3.85

selected_fruit = 0
fruit_price = "error"

if day_of_the_week == "Monday":
    if fruit == "apple":
        selected_fruit = apple
    elif fruit == "banana":
        selected_fruit = banana
    elif fruit == "orange":
        selected_fruit = orange
    elif fruit == "grapefruit":
        selected_fruit = grapefruit
    elif fruit == "kiwi":
        selected_fruit = kiwi
    elif fruit == "pineapple":
        selected_fruit = pineapple
    elif fruit == "grapes":
        selected_fruit = grapes
elif day_of_the_week == "Tuesday":
    if fruit == "apple":
        selected_fruit = apple
    elif fruit == "banana":
        selected_fruit = banana
    elif fruit == "orange":
        selected_fruit = orange
    elif fruit == "grapefruit":
        selected_fruit = grapefruit
    elif fruit == "kiwi":
        selected_fruit = kiwi
    elif fruit == "pineapple":
        selected_fruit = pineapple
    elif fruit == "grapes":
        selected_fruit = grapes
elif day_of_the_week == "Wednesday":
    if fruit == "apple":
        selected_fruit = apple
    elif fruit == "banana":
        selected_fruit = banana
    elif fruit == "orange":
        selected_fruit = orange
    elif fruit == "grapefruit":
        selected_fruit = grapefruit
    elif fruit == "kiwi":
        selected_fruit = kiwi
    elif fruit == "pineapple":
        selected_fruit = pineapple
    elif fruit == "grapes":
        selected_fruit = grapes
elif day_of_the_week == "Thursday":
    if fruit == "apple":
        selected_fruit = apple
    elif fruit == "banana":
        selected_fruit = banana
    elif fruit == "orange":
        selected_fruit = orange
    elif fruit == "grapefruit":
        selected_fruit = grapefruit
    elif fruit == "kiwi":
        selected_fruit = kiwi
    elif fruit == "pineapple":
        selected_fruit = pineapple
    elif fruit == "grapes":
        selected_fruit = grapes
elif day_of_the_week == "Friday":
    if fruit == "apple":
        selected_fruit = apple
    elif fruit == "banana":
        selected_fruit = banana
    elif fruit == "orange":
        selected_fruit = orange
    elif fruit == "grapefruit":
        selected_fruit = grapefruit
    elif fruit == "kiwi":
        selected_fruit = kiwi
    elif fruit == "pineapple":
        selected_fruit = pineapple
    elif fruit == "grapes":
        selected_fruit = grapes
elif day_of_the_week == "Saturday":
        if fruit == "apple":
            selected_fruit = 1.25
        elif fruit == "banana":
            selected_fruit = 2.70
        elif fruit == "orange":
            selected_fruit = 0.90
        elif fruit == "grapefruit":
            selected_fruit = 1.60
        elif fruit == "kiwi":
            selected_fruit = 3.00
        elif fruit == "pineapple":
            selected_fruit = 5.60
        elif fruit == "grapes":
            selected_fruit = 4.20
elif day_of_the_week == "Sunday":
        if fruit == "apple":
            selected_fruit = 1.25
        elif fruit == "banana":
            selected_fruit = 2.70
        elif fruit == "orange":
            selected_fruit = 0.90
        elif fruit == "grapefruit":
            selected_fruit = 1.60
        elif fruit == "kiwi":
            selected_fruit = 3.00
        elif fruit == "pineapple":
            selected_fruit = 5.60
        elif fruit == "grapes":
            selected_fruit = 4.20
else:
    fruit_price = 0

fruit_price = quantity * selected_fruit

if fruit_price == 0:
    fruit_price = "error"
    print(fruit_price)
else:
    print(f"{fruit_price:.2f}")
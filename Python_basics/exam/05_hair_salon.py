goal_for_today = int(input())
command = input()
earned_today = 0
is_goal_reached = False

while command != "closed":
    haircut = command
    customer_type = input()
    if haircut == "haircut" or haircut == "color":
        if customer_type == "mens":
            price = 15
        elif customer_type == "ladies":
            price = 20
        elif customer_type == "kids":
            price = 10
        elif customer_type == "touch up":
            price = 20
        elif customer_type == "full color":
            price = 30
    earned_today += price
    if earned_today >= goal_for_today:
        is_goal_reached = True
        break

    command = input()

missing_amount = goal_for_today - earned_today

if is_goal_reached:
    print(f"You have reached your target for the day!")

else:
    print(f"Target not reached! You need {missing_amount}lv. more.")

print(f"Earned money: {earned_today}lv.")

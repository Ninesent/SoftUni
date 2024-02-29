easter_cakes = int(input())
best_result_name = ""
best_points = 0

for easter_cake in range(easter_cakes):
    personal_points = 0
    cook_name = input()
    command = input()

    while command != "Stop":
        easter_cake_value = int(command)
        personal_points += easter_cake_value

        command = input()
    print(f"{cook_name} has {personal_points} points.")
    if personal_points > best_points:
        best_points = personal_points
        best_result_name = cook_name
        print(f"{cook_name} is the new number 1!")

print(f"{cook_name} won competition with {best_points} points!")
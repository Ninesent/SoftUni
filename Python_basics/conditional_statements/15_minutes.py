hour = int(input())
minutes = int(input())

TIME_FORWARD = 15

minutes_after = minutes + TIME_FORWARD


if minutes_after > 59:
    minutes_after %= 60
    hour += 1
    new_hour = hour % 24
    print(f"{new_hour}:{minutes_after :02d}")
else:
    print(f"{hour}:{minutes_after}")


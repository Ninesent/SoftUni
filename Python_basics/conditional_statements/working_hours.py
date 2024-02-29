hour = int(input())
day_of_the_week = input()

working_status = "closed"

if day_of_the_week == "Monday":
    if 10 <= hour and hour <= 18:
        working_status = "open"
elif day_of_the_week == "Tuesday":
    if 10 <= hour and hour <= 18:
        working_status = "open"
elif day_of_the_week == "Wednesday":
    if 10 <= hour and hour <= 18:
        working_status = "open"
elif day_of_the_week == "Thursday":
    if 10 <= hour and hour <= 18:
        working_status = "open"
elif day_of_the_week == "Friday":
    if 10 <= hour and hour <= 18:
        working_status = "open"
elif day_of_the_week == "Saturday":
    if 10 <= hour and hour <= 18:
        working_status = "open"

print(working_status)
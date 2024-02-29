from math import ceil

LUNCH = 8
RELAX = 4

serial_name = str(input())
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / LUNCH
relax_time = break_length / RELAX

total_time = episode_length + lunch_time + relax_time

if break_length >= total_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(break_length - total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(total_time - break_length)} more minutes.")
from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

sum = time_first + time_second + time_third
minutes = sum // 60
seconds = sum % 60
minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
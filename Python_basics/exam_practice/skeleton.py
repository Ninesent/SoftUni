minutes_control = int(input())
seconds_control = int(input())
length_in_meters = float(input())
seconds_for_hundred_meters = int(input())
control_in_seconds = minutes_control * 60 + seconds_control
reduction_in_seconds = length_in_meters / 120 * 2.5
total_time = length_in_meters / 100 * seconds_for_hundred_meters - reduction_in_seconds

if total_time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    difference = total_time - control_in_seconds
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
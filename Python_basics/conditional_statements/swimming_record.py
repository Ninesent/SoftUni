record_in_seconds = float(input())
distance_in_meteres = float(input())
time_per_one_meter = float(input())

from math import floor

time_needed = distance_in_meteres * time_per_one_meter

if distance_in_meteres >= 15:
    delay = floor(distance_in_meteres / 15) * 12.5
    final_time = time_needed + delay

else:
    final_time = time_needed

if record_in_seconds <= final_time:
    print(f"No, he failed! He was {final_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")




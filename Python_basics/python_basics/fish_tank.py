length = int(input())
width = int(input())
height = int(input())
empty_space_percent = float(input()) / 100

total_volume = length * width * height # cm^3
total_volume_in_liters = total_volume / 1000

water_needed = total_volume_in_liters * (1 - empty_space_percent)

print(water_needed)
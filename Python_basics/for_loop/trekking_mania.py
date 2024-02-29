groups = int(input())

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for n in range(groups):
    current_number = int(input())
    if current_number <= 5:
        musala += current_number
    elif 6 <= current_number <= 12:
        mont_blanc += current_number
    elif 13 <= current_number <= 25:
        kilimanjaro += current_number
    elif 26 <= current_number <= 40:
        k2 += current_number
    elif current_number >= 41:
        everest += current_number

total_people = everest + k2 + kilimanjaro + mont_blanc + musala

musala_climbers = musala / total_people * 100
mont_blanc_climbers = mont_blanc / total_people * 100
kilimanjaro_climbers = kilimanjaro / total_people * 100
k2_climbers = k2 / total_people * 100
everest_climbers = everest / total_people * 100

print(f"{musala_climbers :.2f}%")
print(f"{mont_blanc_climbers :.2f}%")
print(f"{kilimanjaro_climbers:.2f}%")
print(f"{k2_climbers :.2f}%")
print(f"{everest_climbers :.2f}%")

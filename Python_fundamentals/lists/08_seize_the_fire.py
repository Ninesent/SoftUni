list_fires_cells = input().split("#")
water = int(input())
effort = 0.0
total_fire = 0
list_extinguished: list = ["Cells:"]

for cell in list_fires_cells:

    l_cell = cell.split(" = ")

    if l_cell[0] == "High" and 81 <= int(l_cell[1]) <= 125 and water - int(l_cell[1]) >= 0:

        list_extinguished.append(" - " + l_cell[1])
        effort += int(l_cell[1]) * 0.25
        water -= int(l_cell[1])
        total_fire += int(l_cell[1])

    elif l_cell[0] == "Medium" and 51 <= int(l_cell[1]) <= 80 and water - int(l_cell[1]) >= 0:

        list_extinguished.append(" - " + l_cell[1])
        effort += int(l_cell[1]) * 0.25
        water -= int(l_cell[1])
        total_fire += int(l_cell[1])

    elif l_cell[0] == "Low" and 1 <= int(l_cell[1]) <= 50 and water - int(l_cell[1]) >= 0:

        list_extinguished.append(" - " + l_cell[1])
        effort += int(l_cell[1]) * 0.25
        water -= int(l_cell[1])
        total_fire += int(l_cell[1])

print(*list_extinguished, sep="\n")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
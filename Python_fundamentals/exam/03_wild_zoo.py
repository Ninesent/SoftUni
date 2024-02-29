command = input()
animals_dict = {}
area_dict = {}
while command != "EndDay":
    command = command.split()

    if command[0] == "Add:":
        animal_name, needed_food, area = command[1].split("-")
        if not animal_name in animals_dict.keys():
            animals_dict[animal_name] = int(needed_food)
            if not area in area_dict.keys():
                area_dict[area] = []
            area_dict[area].append(animal_name)
        else:
            animals_dict[animal_name] += int(needed_food)

    elif command[0] == "Feed:":
        animal_name, food = command[1].split("-")
        food = int(food)
        if animal_name in animals_dict.keys():
            animals_dict[animal_name] -= int(food)
            if animals_dict[animal_name] <= 0:
                print(f"{animal_name} was successfully fed")
                animals_dict.pop(animal_name)
                copy_area = area_dict.copy()
                for enclosure, animal_list in copy_area.items():
                    for animal in animal_list:
                        if not animal in animals_dict.keys():
                            copy_area[enclosure].remove(animal)
                        if not animal_list:
                            del area_dict[enclosure]

    command = input()

print("Animals:")

for animal, food in animals_dict.items():
    print(f" {animal} -> {food}g")

print("Areas with hungry animals:")

for enclosure, animal_list in area_dict.items():
    print(f" {enclosure}: {len(animal_list)}")
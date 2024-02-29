coffee_stock = input().split()
command_count = int(input())


def include_coffee(coffee_list: list, coffee_name: str) -> list:
    coffee_list.append(coffee_name)
    return coffee_list


def remove_coffee(coffee_list: list, place: str, amount_to_remove: int) -> list:
    remove_counter = 0
    if place == "first" and len(coffee_list) > amount_to_remove:
        for coffee_removal in range(amount_to_remove):
            coffee_list.pop(remove_counter)
    elif place == "last" and len(coffee_list) > amount_to_remove:
        for coffee_removal in range(amount_to_remove):
            remove_counter = -1
            coffee_list.pop(remove_counter)

    return coffee_list


def preferred_coffee(coffee_list: list, index1: int, index2: int) -> list:
    if 0 <= index1 < len(coffee_list) and 0 <= index2 < len(coffee_list):
        coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]

    return coffee_list


for coffee in range(command_count):
    command = input().split()

    if command[0] == "Include":
        coffee_name = command[1]
        include_coffee(coffee_stock, coffee_name)

    elif command[0] == "Remove":
        remove_coffee(coffee_stock, command[1], int(command[2]))

    elif command[0] == "Prefer":
        preferred_coffee(coffee_stock, int(command[1]), int(command[2]))

    elif command[0] == "Reverse":
        coffee_stock.reverse()

print("Coffees:")
print(" ".join(coffee_stock))

gifts = input().split()
gifts_list = gifts.copy()

command = input().split()

while command != ["No", "Money"]:

    command_type = command[0]
    gift_type = command[1]

    if command_type == "OutOfStock":
        while gift_type in gifts_list:
            find_index = gifts_list.index(gift_type)
            gifts_list[find_index] = None
    elif command_type == "Required":
        gift_index = int(command[2])
        if 0 <= gift_index < len(gifts_list):
            gifts_list[gift_index] = gift_type
    elif command_type == "JustInCase":
        gifts_list[-1] = gift_type

    command = input().split()

while None in gifts_list:
    gifts_list.remove(None)

print(" ".join(gifts_list))
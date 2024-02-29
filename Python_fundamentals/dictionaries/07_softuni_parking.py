number_of_commands = int(input())

parking_lot = {}

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == "register":
        name = command[1]
        license_plate = command[2]
        if name in parking_lot.keys() and parking_lot[name] == license_plate:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[name] = license_plate
            print(f"{name} registered {license_plate} successfully")


    elif command[0] == "unregister":
        name = command[1]

        if name in parking_lot.keys():
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, license_plate in parking_lot.items():
    print(f"{name} => {license_plate}")

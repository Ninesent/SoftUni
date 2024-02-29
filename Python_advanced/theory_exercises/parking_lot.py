n = int(input())

cars = set()

for _ in range(n):

    direction, car_number = input().split()

    if direction == "IN":
        cars.add(car_number)

    elif direction == "OUT":
        cars.remove(car_number)


if cars:
    for car in cars:
        print(cars)
else:
    print("Parking lot is empty")
figure_type = input()

if figure_type == "square":
        side = float(input())
        area = side * side
        print(f"{area:.3f}")

elif figure_type == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
    print(f"{area:.3f}")

elif figure_type == "circle":
    radius = float(input())
    from math import pi
    area = pi * radius ** 2
    print(f"{area:.3f}")

elif figure_type == "triangle":
    length = float(input())
    height = float(input())
    area = length * height / 2
    print(f"{area:.3f}")


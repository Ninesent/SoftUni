first_multi = 1
second_multi = 1

while first_multi < 11:
    second_multi = 1
    while second_multi < 11:
        print(f"{first_multi} * {second_multi} = {first_multi * second_multi}")
        second_multi += 1
    first_multi += 1
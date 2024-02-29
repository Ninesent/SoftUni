number = int(input())
is_found = False
is_found_two = False

for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(9):
            for d in range(9, c, -1):
                for e in range(1, 9):
                    for f in range(9, e, -1):
                        for g in range(9):
                            for i in range(9, g, -1):
                                if a == e and b == f and c == g and d == i:
                                    multiply_result = e * f * g * i
                                    plus_result = a + b + c + d
                                    if multiply_result == plus_result and multiply_result % 10 == 5:
                                        print(f"{a}{b}{c}{d}")
                                        is_found_two = True

                                    if multiply_result // plus_result == 3 and number % 3 == 0:
                                        is_found = True
                                        if is_found:
                                            break


    if is_found or is_found_two:
        break

if is_found:
    print(f"{d}{c}{b}{a}")
else:
    print(f"Nothing found")



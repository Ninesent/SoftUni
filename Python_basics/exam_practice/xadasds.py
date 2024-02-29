number = int(input())
is_found_one = False

for x1 in range(1, 10):
    if is_found_one:
        break
    for x2 in range(9, x1, -1):
        if is_found_one:
            break
        for x3 in range(9):
            if is_found_one:
                break
            for x4 in range(9, x3, -1):
                if is_found_one:
                    break
                for x5 in range(1, 10):
                    if is_found_one:
                        break
                    for x6 in range(9, x5, -1):
                        if is_found_one:
                            break
                        for x7 in range(9):
                            if is_found_one:
                                break
                            for x8 in range(9, x7, -1):
                                if is_found_one:
                                    break
                                if x1 == x5 and x2 == x6 and x3 == x7 and x4 == x8:
                                    multiply_result = x1 * x2 * x3 * x4
                                    plus_result = x5 + x6 + x7 + x8
                                    if multiply_result == plus_result and number % 10 == 5:
                                        is_found_one = True
                                        print(f"{x1}{x2}{x3}{x4}")
                                        break
                                    elif multiply_result // plus_result == 3 and number % 3 == 0:
                                        is_found_one = True
                                        if is_found_one:
                                            print(f"{x8}{x7}{x6}{x5}")
                                            break

if not is_found_one:
    print(f"Nothing found")

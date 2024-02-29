pair_of_rows = int(input())

student_dict = {}
for _ in range(pair_of_rows):
    name = input()
    grade = float(input())

    if not name in student_dict.keys():
        student_dict[name] = []
    student_dict[name].append(grade)


for name, grades in student_dict.items():

    result = sum(grades) / len(grades)

    if result >= 4.50:
        print(f"{name} -> {result:.2f}")
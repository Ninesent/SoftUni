student_name = input()
hogwarts_house = ""
sorted_successfully = True

while student_name != "Welcome!":
    if student_name == "Voldemort":
        print("You must not speak of that name!")
        sorted_successfully = False
        exit()
    if len(student_name) < 5:
        hogwarts_house = "Gryffindor"
    elif len(student_name) == 5:
        hogwarts_house = "Slytherin"
    elif len(student_name) == 6:
        hogwarts_house = "Ravenclaw"
    elif len(student_name) > 6:
        hogwarts_house = "Hufflepuff"


    print(f"{student_name} goes to {hogwarts_house}." )

    student_name = input()

if sorted_successfully:
    print("Welcome to Hogwarts.")
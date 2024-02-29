course_information = input()

administration = {}

while course_information != "end":

    class_name, student = course_information.split(":")
    class_name, student = class_name.strip(), student.strip()

    if not class_name in administration.keys():
        administration[class_name] = []
    administration[class_name].append(student)

    course_information = input()

for course_name, registered_students in administration.items():
    print(f"{course_name}: {len(registered_students)}")
    for student in registered_students:
        print(f"-- {student}")

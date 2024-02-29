command = input()

company_details = {}

while command != "End":
    company_name, employee = command.split(" -> ")

    if not company_name in company_details.keys():
        company_details[company_name] = []

    if not employee in company_details[company_name]:
        company_details[company_name].append(employee)


    command = input()


for company, employees in company_details.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
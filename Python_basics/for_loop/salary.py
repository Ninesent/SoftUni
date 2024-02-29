facebook = 150
instagram = 100
reddit = 50

tabs_opened = int(input())
salary = float(input())

for tabs in range(tabs_opened):
    current_tabs = input()

    if current_tabs == "Facebook":
        salary -= facebook
    elif current_tabs == "Instagram":
        salary -= instagram
    elif current_tabs == "Reddit":
        salary -= reddit
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{int(salary)}")

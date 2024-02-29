SUCCESSFUL_PROJECT_TIME = 3

architect_name = input()
number_of_projects = int(input())
time_needed_for_completion = number_of_projects * SUCCESSFUL_PROJECT_TIME

print(f"The architect {architect_name} will need {time_needed_for_completion} hours to complete "
      f"{number_of_projects} project/s.")


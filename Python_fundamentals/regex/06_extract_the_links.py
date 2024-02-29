import re


pattern = r"(w{3}\.[a-zA-Z0-9\-\.]+\.[a-z]+)"
line = input()

while line:

    correct_site = re.findall(pattern, line)
    if correct_site:
        print(*correct_site)
    line = input()

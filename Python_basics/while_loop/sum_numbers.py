number = int(input())
new_number = int(input())
request_number = 0


while number > new_number:
    request_number = int(input())
    new_number += request_number

print(new_number)

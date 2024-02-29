password = str(input())
outcome = "none"

if password == "s3cr3t!P@ssw0rd":
    outcome = "Welcome"
else:
    outcome = "Wrong password!"

print(outcome)


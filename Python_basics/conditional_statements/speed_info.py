speed = float(input())
outcome = 0

if speed <= 10:
    outcome = "slow"
elif speed <= 50:
     outcome = "average"
elif speed <= 150:
    outcome = "fast"
elif speed <= 1000:
    outcome = "ultra fast"
elif speed > 1000:
    outcome = "extremely fast"

print(outcome)
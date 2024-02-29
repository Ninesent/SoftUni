experience_needed = float(input())
battle_count = int(input())
is_collected = False
experience_collected = 0


for battle in range(1, battle_count + 1):
    experience = float(input())
    experience_collected += experience
    if battle % 3 == 0:
        experience_collected += experience * 0.15
    if battle % 5 == 0:
        experience_collected -= experience * 0.10
    if battle % 15 == 0:
        experience_collected += experience * 0.5

    if experience_collected >= experience_needed:
        is_collected = True
        break

experience_left = experience_needed - experience_collected

if is_collected:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_left:.2f} more needed.")
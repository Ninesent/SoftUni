from math import floor

win = 2000
final = 1200
semi_final = 720

tournaments = int(input())
starting_points = int(input())

gained_points = 0
total_wins = 0

for _ in range(tournaments):
    tournament_result = input()
    if tournament_result == "W":
        gained_points += win
        total_wins += 1
    elif tournament_result == "F":
        gained_points += final
    elif tournament_result == "SF":
        gained_points += semi_final

total_points = starting_points + gained_points
avg_points = floor(gained_points / tournaments)
win_percent = total_wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{win_percent :.2f}%")

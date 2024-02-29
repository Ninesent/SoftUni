annual_fee = int(input())

basketball_shoes = annual_fee - (annual_fee * 0.40)
basketball_suit = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_suit / 4
basketball_accessories = basketball_ball / 5

total_sum = annual_fee + basketball_shoes + basketball_suit + basketball_ball + basketball_accessories

print(total_sum)
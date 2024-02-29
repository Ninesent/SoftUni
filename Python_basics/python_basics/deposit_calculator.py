deposit_amount = float(input())
deposit_timeframe = int(input())
yearly_interest = float(input()) / 100
final_sum = deposit_amount + deposit_timeframe * ((deposit_amount * yearly_interest)/12)

print(final_sum)



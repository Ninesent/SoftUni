one_night = 20
transport_card = 1.60
museum_ticket = 6

group_amount = int(input())
booked_nights = int(input())
transport_cards_amount = int(input())
museum_tickets_amount = int(input())

total_cost = (booked_nights * one_night) + (transport_cards_amount * transport_card) + \
               (museum_ticket * museum_tickets_amount)

total_amount = total_cost * group_amount * 1.25

print(f"{total_amount:.2f}")
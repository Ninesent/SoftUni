packet_of_pencils = float(input()) * 5.80
packet_of_markers = float(input()) * 7.20
cleaning_spray = float(input()) * 1.20
discount = float(input()) / 100
discount_amount = (packet_of_pencils + packet_of_markers + cleaning_spray) * discount

total = print(packet_of_pencils + packet_of_markers + cleaning_spray - discount_amount)



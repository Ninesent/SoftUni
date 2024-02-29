NYLON = 1.50
PAINT = 14.50
PAINT_THINNER = 5.00
BAG = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hours_needed = int(input())

extra_paint = paint_quantity * 0.1
extra_nylon = 2

total_material_cost = (nylon_quantity + extra_nylon) * NYLON + (paint_quantity + extra_paint) * \
                      PAINT + (paint_thinner_quantity * PAINT_THINNER) + BAG


worker_cost = total_material_cost * 0.30

total_price = total_material_cost + worker_cost * work_hours_needed

print(total_price)
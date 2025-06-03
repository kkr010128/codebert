input_str = input().split()
amount_to_make = int(input_str[0])
lot_size = int(input_str[1])
time_to_make_one_lot = int(input_str[2])

proceeded_time = 0
made_amount = 0
while made_amount < amount_to_make:
    made_amount += lot_size
    proceeded_time += time_to_make_one_lot

print(proceeded_time)

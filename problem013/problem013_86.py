data_num = int(input())
cnt = 0
deff_price = -999999999
min_price = 0
tmp_price = 0

for i in range(data_num):
    price = int(input())
 
    if i ==0:
        min_price = price
    elif price - min_price > deff_price:
        deff_price = price - min_price
    
    if price < min_price:
        min_price = price

print(str(deff_price))
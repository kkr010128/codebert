input_n = input()
price1  = input()
price2  = input()
min_price = min(price1,price2)
max_profit = price2-price1
for i in xrange(input_n-2):
    input_profit = input()
    tmp = input_profit-min_price
    if max_profit<tmp:
        max_profit = tmp
    if min_price>input_profit:
        min_price = input_profit
print max_profit
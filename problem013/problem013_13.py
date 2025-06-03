n = int(input())

maximum_profit = -10**9
r0 = int(input())
r_min = r0
for i in range(1, n):
    r1 = int(input())
    if r0 < r_min:
        r_min = r0
    profit = r1 - r_min
    if profit > maximum_profit:
        maximum_profit = profit
    r0 = r1
print(maximum_profit)
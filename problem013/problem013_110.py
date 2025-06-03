# ??\?????????
N = int(input())
r = [int(input()) for i in range(N)]

# ?????§????¨????
max_profit = (-1) * (10 ** 9)
min_value = r[0]
for j in range(1, len(r)):
    max_profit = max(max_profit, r[j] - min_value)
    min_value = min(min_value, r[j])
print(max_profit)
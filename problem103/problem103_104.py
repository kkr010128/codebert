n = int(input())
a = list(map(int, input().split())) + [0]

buy, sell = [], []
for i in range(n):
    if a[i] < a[i+1] and len(buy) - len(sell) == 0:
        buy.append(i)
    if len(buy) - len(sell) == 1 and a[i] > a[i+1]:
        sell.append(i)

cash = 1000
for i, j in zip(buy, sell):
    stock, rest = divmod(cash, a[i])
    cash = stock * a[j] + rest

print(cash)
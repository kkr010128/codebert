n = int(input())
a = list(map(int, input().split()))

d = {}
d[0] = 1000

for i in range(n):
    e = d.copy()
    for stock, money in e.items():
        # sell
        d[0] = max(d[0], money + stock * a[i])
        # buy
        k = money // a[i]
        stock += k
        money -= k * a[i]
        d[stock] = max(d.get(stock, 0), money)

print(d[0])
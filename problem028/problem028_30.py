INF = 10**8

n, m = map(int, input().split())
c = list(map(int, input().split()))

d = [INF] * (n + 1)
d[0] = 0

for coin in c:
	for price in range(coin, n + 1):
		d[price] = min(d[price], d[price - coin] + 1)

print(d[n])

n = int(input())
inf = 10 ** 10
buy = inf
ans = -inf
for i in range(n):
    price = int(input())
    ans = max(ans, price - buy)
    buy = min(buy, price)
print(ans)


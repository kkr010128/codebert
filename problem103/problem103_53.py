n = int(input())
a = list(map(int, input().split()))

cash = 1000

for buy, sell in zip(a, a[1:]):
    if buy >= sell:
        continue
    stock, cash = divmod(cash, buy)
    cash += stock * sell

print(cash)
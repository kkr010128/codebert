n = int(input())
a = list(map(int, input().split()))

def buy(money, stock, p):
    amount = money // p
    return (money - amount * p), amount

def sell(money, stock, p):
    return (money + stock * p), 0

money = 1000
stock = 0
for i, (p, q) in enumerate(zip(a[:-1], a[1:])):
    if stock == 0 and p < q:
        money, stock = buy(money, stock, p)
    elif stock and p > q:
        money, stock = sell(money, stock, p)

if stock:
    money += stock * a[-1]

print(money)

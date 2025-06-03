INF = 300

n = int(input())
a = [INF] + list(map(int, input().split())) + [-INF]

money = 1000
stock = 0
for e1, e2 in zip(a, a[1:]):
    if e1 < e2:
        buy = money // e1
        money -= buy * e1
        stock += buy
    else:
        money += stock * e1
        stock = 0

print(money)

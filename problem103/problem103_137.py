n, *a = map(int, open(0).read().split())
max_a = max(a)
money = 1000
stock = 0
for i in range(n-1):
    if a[i] < a[i+1]:
        stock = money // a[i]
        money += (a[i+1] - a[i]) * stock
print(money)
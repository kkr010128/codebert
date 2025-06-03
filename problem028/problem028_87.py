n =int(input().split()[0])
m = map(int, input().split())

c = [ i for i in range(n+1) ]
coins = []

for coin in m:
    if coin <= n:
        c[coin] = 1
        coins.append(coin)

for p in range(2,n+1):
    minc = c[p]
    if minc <= 2:
        continue
    for coin in coins:
        if p > coin:
            if minc > c[p-coin]+1:
                minc = c[p-coin]+1
    c[p] = minc

print(c[n])
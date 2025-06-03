n, m, x = map(int, input().split())

c = [0] * n
a = [[0] * m for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    c[i] = tmp[0]
    a[i] = tmp[1:]

INF = 10 ** 9
ans = INF

for i in range(1 << n):
    cost = 0
    under = [0] * m
    for j in range(n):
        if not i >> j & 1: continue
        cost += c[j]
        for k in range(m):
            under[k] += a[j][k]
    ok = True
    for k in range(m):
        if under[k] < x: ok = False
    if ok:
        ans = min(ans, cost)

if ans == INF: print("-1")
else: print(ans)
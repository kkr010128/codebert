n,m,x = map(int,input().split())
ca = [list(map(int,input().split())) for i in range(n)]

c = [0]*n
a = [0]*n

for i in range(n):
    c[i],a[i] = ca[i][0],ca[i][1:]

INF = 10**9
ans  = INF

for i in range(1<<n):
    understanding = [0]*m
    cost = 0
    for j in range(n):
        if ((i>>j)&1):
            cost += c[j]
            for k in range(m):
                understanding[k] += a[j][k]
    ok = True
    for s in range(m):
        if understanding[s] < x:
            ok = False
    if ok:
        ans = min(ans, cost)

if ans == INF:
    ans = -1

print(ans)

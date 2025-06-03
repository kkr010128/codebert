n, m, x = map(int,input().split())
c = [0] *(n)
a = [[0] for _ in range(n)]

ans = 10**10

for i in range(n):
    ca = list(map(int,input().split()))
    c[i] = ca[0]
    a[i] = ca[1:]

for i in range(1 << n):
    skill = [0] * m
    total_cost = 0
    for j in range(n):
        if (i>>j) & 1:
            total_cost += c[j]
            skill = [skill[t] + a[j][t] for t in range(m)]
    if all (y >= x for y in skill):
        ans = min(ans, total_cost)

if ans == 10**10:
    print(-1)
else:
    print(ans)
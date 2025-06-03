n, m, x = map(int, input().split())
book = [list(map(int, input().split())) for i in range(n)]

min_num = 10**18

for i in range(1<<n):
    cost = 0
    l = [0]*m
    for j in range(n):
        if (i>>j)&1:
            c, *a = book[j]
            cost += c
            for k ,ak in enumerate(a):
                l[k] += ak
    if all(lj >= x for lj in l):
        min_num = min(min_num,cost)

print(-1 if min_num == 10**18 else min_num)

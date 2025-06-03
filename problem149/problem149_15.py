n, m, x = map(int, input().split())
c = []
algo = []
for _ in range(n):
    l = list(map(int, input().split()))
    c.append(l[0])
    algo.append(l[1:])

cost = []
for i in range(2**n):
    c_sum = 0
    u_sum = [0]*m
    for j in range(n):
        if (i>>j) & 1:
            c_sum += c[j]
            for k in range(m):
                u_sum[k] += algo[j][k]
    if all(s >= x for s in u_sum):
        cost.append(c_sum)
if cost:
    print(min(cost))
else:
    print(-1)

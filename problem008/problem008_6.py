def depth_search(i, adj, d, f, t):
    if d[i - 1]:
        return t
    d[i - 1] = t
    t += 1
    for v in adj[i - 1]:
        t = depth_search(v, adj, d, f, t)
    f[i - 1] = t
    t += 1
    return t
n = int(input())
adj = [list(map(int, input().split()))[2:] for _ in range(n)]

d = [0] * n
f = [0] * n

t = 1
for i in range(n):
    if d[i] == 0:
        t = depth_search(i + 1, adj, d, f, t)

for i, df in enumerate(zip(d, f)):
    print(i + 1, *df)   
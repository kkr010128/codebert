# Peaks

n, m = map(int, input().split())
h = [0] + list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = 0
for v in range(1, n+1):
    for u in g[v]:
        if h[v] <= h[u]:
            break
    else:
        ans += 1

print(ans)

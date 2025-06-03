n, m = map(int,input().split())
h = list(map(int, input().split()))
e = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    e[u].append(h[u]- h[v])
    e[v].append(h[v]- h[u])

cnt = 0
for i in range(n):
    if not e[i]:
        cnt += 1
    elif min(e[i]) > 0:
        cnt += 1
print(cnt)
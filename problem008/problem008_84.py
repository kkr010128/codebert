N = int(input())
edge = [[] for _ in range(N+1)]
d = [0] * (N+1)
f = [0] * (N+1)
for i in range(N):
    t = list(map(int, input().split()))
    for j in range(t[1]):
        edge[t[0]].append(t[j+2])

#print(1)
def dfs(v, t):
    if d[v] == 0:
        d[v] = t
        t += 1
    else:
        return t
    for nv in edge[v]:
        t = dfs(nv, t)
    if f[v] == 0:
        f[v] = t
        t += 1
    return t

t = 1
for i in range(1,1+N):
    if d[i] == 0:
        t = dfs(i, t)
for i in range(1,1+N):
    print(i, d[i], f[i])


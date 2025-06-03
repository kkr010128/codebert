def inpl():
    return list(map(int, input().split()))


def dfs(v, step):
    if f[v] != -1:
        return step
    f[v] = step
    step += 1
    for nv in E[v]:
        # print("now", v, nv, step)
        step = dfs(nv - 1, step)
    d[v] = step
    return step + 1


n = int(input())
E = [[] for i in range(n)]
for _ in range(n):
    tmp = inpl()
    u, k = tmp[:2]
    E[u - 1] = tmp[2:]

d = [-1 for i in range(n)]
f = [-1 for i in range(n)]

step = 1
for v in range(n):
    step = dfs(v, step)

for i in range(n):
    print(i + 1, f[i], d[i])


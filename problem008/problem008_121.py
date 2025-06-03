n = int(input())
g = [None] * n
visited = [0] * n
root = set(range(n))
ts = [[0, 0] for _ in range(n)]
t = 0

while n:
    l = list(map(int, input().split()))
    connected = [i - 1 for i in l[2:]]
    g[l[0] - 1] = [i - 1 for i in l[2:]]
    root -= set(connected)
    n -= 1


def dfs(i):
    global g, t, ts, visited
    lts = ts[i]
    t += 1
    lts[0] = t
    visited[i] = 1
    for c in g[i]:
        if not visited[c]:
            dfs(c)
    t += 1
    lts[1] = t

if root:
    for r in sorted(root):
        dfs(r)
else:
    dfs(0)

for i, v in enumerate(ts):
    print(i + 1, *v)
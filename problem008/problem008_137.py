import sys
sys.setrecursionlimit(10000000)
n = int(input())
G = [[] for i in range(n)]
d = [0 for i in range(n)]
f = [0 for i in range(n)]
color = [0 for i in range(n)]
stamp = 0

def dfs(u):
    global stamp
    if d[u]:
        return
    stamp += 1
    d[u] = stamp
    for v in G[u]:
        if color[v] != 0:
            continue
        color[v] = 1
        dfs(v)
    color[u] = 2
    stamp += 1
    f[u] = stamp

color[0] = 1
for i in range(n):
    inp = list(map(int, input().split()))
    u = inp[0]
    u -= 1
    k = inp[1]
    for j in range(k):
        v = inp[j+2]
        v -= 1
        G[u].append(v)
        #G[v].append(u)


for i in range(n):
    dfs(i)

for i in range(n):
    print("{0} {1} {2}".format(i+1, d[i], f[i]))

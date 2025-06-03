n = int(input())
graph = [-1] + [list(map(int, input().split())) for _ in range(n)]
seen = [False]*(n+1)
seen[0] = True
d = [-1]*(n+1)
f = [-1]*(n+1)
time = 0


def dfs(v):
    global time
    time += 1
    d[v] = time
    seen[v] = True
    k = graph[v][1]
    if k > 0:
        for i in range(k):
            w = graph[v][i+2]
            if seen[w] is False:
                dfs(w)
    
    time += 1
    f[v] = time

v = 0
while v <= n:
    if seen[v] is False:
        dfs(v)
    
    v += 1

for i in range(1, n+1):
    print(i, d[i], f[i])

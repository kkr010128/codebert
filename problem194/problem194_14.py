from heapq import heappop, heappush

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

def dijkstra(graph, n, s):
    d = [float("inf")] * n
    d[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        dist, v = heappop(q)
        if d[v] < dist: continue
        for nv, cost in graph[v]:
            if d[nv] > d[v] + cost:
                d[nv] = d[v] + cost
                heappush(q, (d[nv], nv))
    return d

n = h*w+1
g = [list() for _ in range(n)]
for i in range(h):
    for j in range(w-1):
        cid = i*w + j
        g[cid].append((cid+1, int(s[i][j] == "." and s[i][j+1] == "#")))
for i in range(h-1):
    for j in range(w):
        cid = i*w + j
        g[cid].append((cid+w, int(s[i][j] == "." and s[i+1][j] == "#")))
g[n-1].append((0, int(s[0][0] == "#")))

print(dijkstra(g, n, n-1)[n-2])

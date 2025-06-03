from collections import defaultdict, deque

N, u, v = map(int, input().split())
G = defaultdict(lambda: [])

for _ in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)


if G[u] == [v]:
    print(0)
    exit()


def bfs(v):
    seen = [0]*(N+1)
    queue = deque()
    dist = [-1]*(N+1)
    dist[v] = 0
    seen[v] = 1
    queue.append(v)
    while queue:
        q = queue.popleft()
        for nx in G[q]:
            if seen[nx]:
                continue
            dist[nx] = dist[q] + 1
            seen[nx] = 1
            queue.append(nx)
    return dist

d_u = bfs(u)
d_v = bfs(v)
ans = 0
for node in range(1, N+1):
    if d_u[node] < d_v[node] and len(G[node]) == 1:
        ans = max(ans, d_v[node]-1)
print(ans)
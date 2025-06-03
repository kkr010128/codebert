n, u, v = map(int, input().split())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dist1 = [100005]*(n+1)

q = []
q.append(v)
dist1[v] = 0
while q:
    now = q.pop()
    for next in tree[now]:
        if dist1[next] == 100005:
            q.append(next)
            dist1[next] = dist1[now] + 1


dist2 = [100005]*(n+1)

q = []
q.append(u)
dist2[u] = 0
while q:
    now = q.pop()
    for next in tree[now]:
        if dist2[next] == 100005:
            q.append(next)
            dist2[next] = dist2[now] + 1

for i in range(1, n+1):
    if dist1[i] <= dist2[i]:
        dist2[i] = -1

for i in range(1, n+1):
    if dist2[i] != -1:
        dist2[i] = 100005

q = []
q.append(u)
dist2[u] = 0
while q:
    now = q.pop()
    for next in tree[now]:
        if dist2[next] == 100005:
            q.append(next)
            dist2[next] = dist2[now] + 1



ans = 0
for i in range(1, n+1):
    if dist2[i] != -1:
        ans = max(ans, dist1[i])

print(ans-1)

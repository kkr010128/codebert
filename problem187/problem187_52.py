from collections import defaultdict

N, X, Y = map(int, input().split())
INF = 10**20
ans = {i:0 for i in range(N)}
d = defaultdict(list)

for i in range(1, N):
    d[i].append(i+1)
    d[i+1].append(i)
d[X].append(Y)
d[Y].append(X)

for i in range(1, N+1):
    dist = [-1]*(N+1)
    q = [i]
    dist[i] = 0

    while q:
        a = q.pop()
        for b in d[a]:
            if dist[b]==-1 or dist[b] > dist[a]+1:
                dist[b] = dist[a] + 1
                q.append(b)
    for j in range(i+1, N+1):
        ans[dist[j]] += 1

for i in range(1,N):
    print(ans[i])
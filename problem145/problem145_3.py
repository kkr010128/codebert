n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

ans = [-1] * n
from collections import deque
d = deque([0])
while d:
    u = d.popleft()
    for v in G[u]:
        if ans[v] == -1:
            ans[v] = u
            d.append(v)

if -1 in ans[1:]:
    print('No')
else:
    print('Yes')
    for v in ans[1:]:
        print(v + 1)

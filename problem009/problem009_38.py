from collections import deque
from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for i in range(n):
    u, k, *v = map(int, input().split())
    for v in v:
        graph[u].append(v)

ans = [-1] * (n + 1)

q = deque([1])
ans[1] = 0

while q:
    c = q.popleft()
    for v in graph[c]:
        if ans[v] == -1:
            ans[v] = ans[c] + 1
            q.append(v)

for i in range(1, n + 1):
    print(i, ans[i])

from collections import deque

def bfs(s):
    visit[i] = 1
    q = deque()
    q.append(s)
    while q:
        p = q.popleft()
        for j in G[p]:
            if not visit[j]:
                visit[j] = 1
                q.append(j)
    return

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visit = [0] * (n + 1)
ans = -1
for i in range(1, n + 1):
    if not visit[i]:
        bfs(i)
        ans += 1
print(ans)
from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
seen = [-1] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(x):
    q = deque([])

    q.append(x)
    seen[x] = 1

    while q:
        x = q.popleft()

        for y in graph[x]:
            if seen[y] != -1:
                continue

            seen[y] = 1
            q.append(y)


ans = 0

for i in range(N):
    if seen[i] != -1:
        continue
    else:
        ans += 1
        bfs(i)

print(ans - 1)

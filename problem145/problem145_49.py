from collections import deque

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
for a, b in X:
    graph[a].append(b)
    graph[b].append(a)

prevs = [-1] * (N + 1)
prevs[1] = 0
q = deque([1])

while q:
    u = q.popleft()
    for v in graph[u]:
        if prevs[v] < 0:
            prevs[v] = u
            q.append(v)
            
print("Yes")
print(*prevs[2:], sep="\n")

from collections import deque
n = int(input())
G = [[] for _ in range(n)]
for i in range(n):
    u, k, *vs = map(int, input().split())
    u -= 1
    vs = list(map(lambda x: x - 1, vs))
    for v in vs:
        G[u].append(v)

dist = [-1] * n
dist[0] = 0
que = deque([0])

while len(que) > 0:
    now_v = que.popleft()
    now_dist = dist[now_v]
    next_vs = G[now_v]
    for next_v in next_vs:
        if dist[next_v] == -1:
            dist[next_v] = now_dist + 1
            que.append(next_v)

for i, x in enumerate(dist):
    print(i + 1, x)

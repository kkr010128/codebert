from collections import deque


def bfs(start):
    Q = deque()
    Q.append(start)
    dist[start] = 0

    while Q:
        v = Q.popleft()

        for nv in G[v]:
            if dist[nv] != -1:
                continue

            # print(Q)
            dist[nv] = dist[v] + 1
            Q.append(nv)


N = int(input())

G = [[]] + [list(map(int, input().split())) for _ in range(N)]
for a in range(1, N + 1):
    b = G[a][2:]
    G[a] = b

# print(G)
dist = [-1 for _ in range(N + 1)]

start = 1
bfs(start)
# print(dist[1:])
for i in range(1, N + 1):
    print(i, dist[i])


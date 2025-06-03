import queue

N = int(input())
G = []
for _ in range(N):
    u, n, *K = map(int, input().split())
    G.append((u - 1, [k - 1 for k in K]))

Q = queue.Queue()
Q.put(G[0])
dist = [-1] * N
dist[0] = 0
while not Q.empty():
    U = Q.get()
    for u in U[1]:
        if dist[u] == -1:
            Q.put(G[u])
            dist[u] = dist[U[0]] + 1

for i, time in enumerate(dist):
    print(i + 1, time)


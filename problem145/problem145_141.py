def dijkstra(v, G):
    import heapq

    ret = [10 ** 10] * len(G)
    ret[v] = 0
    q = [(ret[i], i) for i in range(len(G))]
    heapq.heapify(q)

    while len(q):
        tmpr, u = heapq.heappop(q)
        if tmpr == ret[u]:
            for w in G[u]:
                if ret[w] > ret[u] + 1:
                    ret[w] = ret[u] + 1
                    heapq.heappush(q, (ret[w], w))
    return ret


N, M = map(int, input().split())
G, ans = {i: [] for i in range(N)}, [-1] * N
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

d = dijkstra(0, G)
for a in range(N):
    for b in G[a]:
        if d[a] - d[b] == 1:
            ans[a] = b + 1

print("Yes")
for a in ans[1:]:
    print(a)

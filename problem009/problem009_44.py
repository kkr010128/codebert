import queue


def bfs(g, s=1):
    global q

    dist = [-1] * len(g)
    dist[1] = 0
    q = queue.Queue()
    q.put(s)

    while not q.empty():
        v = q.get()
        if not G[v][1]:
            continue
        for vi in G[v][2:]:
            if dist[vi] >= 0:
                continue
            q.put(vi)
            dist[vi] = dist[v] + 1

    return dist


n = int(input())
G = [None]
for i in range(n):
    G.append(list(map(int, input().split())))

d = bfs(G)
for i in range(1, n + 1):
    print('%d %d' % (i, d[i]))

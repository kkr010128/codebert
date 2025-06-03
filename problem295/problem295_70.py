import sys


def naive_dijkstra(links, n, l):
    F30 = (1 << 30) - 1
    INF = 10 ** 18

    refuels = [[-1] * n for _ in range(n)]

    for s in range(n):
        rs = refuels[s]

        dists = [INF] * n
        dists[s] = 0
        remain_nodes = set(range(n))

        for _ in range(n):
            v = -1
            w = INF
            for u in remain_nodes:
                if dists[u] < w:
                    v = u
                    w = dists[u]
            if v == -1:
                break
            remain_nodes.remove(v)

            count = w >> 30
            used = w & F30
            rs[v] = count

            for u, c in links[v]:
                if l - used < c:
                    nw = ((count + 1) << 30) | c
                else:
                    nw = w + c
                if nw < dists[u]:
                    dists[u] = nw

    return refuels


n, m, l = list(map(int, input().split()))
lines = sys.stdin.readlines()

links = [set() for _ in range(n)]

for line in lines[:m]:
    a, b, c = map(int, line.split())
    a -= 1
    b -= 1
    if l < c:
        continue
    links[a].add((b, c))
    links[b].add((a, c))

dists = naive_dijkstra(links, n, l)
buf = []

for line in lines[m + 1:]:
    s, t = map(int, line.split())
    buf.append(dists[s - 1][t - 1])

print('\n'.join(map(str, buf)))

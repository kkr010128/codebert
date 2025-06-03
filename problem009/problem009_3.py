n = int(input())

adj = [None]
for i in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

isSearched = [None] + [False] * n

distance = [None] + [-1] * n

def bfs(u):
    d = 0
    isSearched[u] = True
    distance[u] = d
    edge = [u]
    while edge:
        q = list(edge)
        edge = []
        d += 1
        for c_e in q:
            for n_e in adj[c_e]:
                if not isSearched[n_e]:
                    isSearched[n_e] = True
                    edge.append(n_e)
                    distance[n_e] = d


bfs(1)

for i, x in enumerate(distance[1:], start=1):
    print(i, x)
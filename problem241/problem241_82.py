import networkx as nx

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

G = nx.Graph()
# 辺を加えていく
for h in range(H):
    for w in range(W - 1):
        if maze[h][w] == maze[h][w + 1] == '.':
            G.add_edge((h, w), (h, w + 1))
for h in range(H - 1):
    for w in range(W):
        if maze[h][w] == maze[h + 1][w] == '.':
            G.add_edge((h, w), (h + 1, w))


def bfs(sy, sx):
    d = dict()
    d[(sy, sx)] = 0
    for coordinate_from, coordinate_to in nx.bfs_edges(G, (sy, sx)):
        d[coordinate_to] = d[coordinate_from] + 1
    return max(d.values())


ans = 0
for y in range(H):
    for x in range(W):
        if maze[y][x] == '.':
            ans = max(ans, bfs(y, x))
print(ans)

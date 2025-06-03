import networkx as nx

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

G = nx.grid_2d_graph(H, W)
for h in range(H):
    for w in range(W):
        # 壁に入る辺を削除
        if maze[h][w] == '#':
            for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if ((h - dh, w - dw), (h, w)) in G.edges():
                    G.remove_edge((h - dh, w - dw), (h, w))


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

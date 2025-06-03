n = input()

d     = [0 for i in range(n)]
f     = [0 for i in range(n)]
G     = [0 for i in range(n)]
M     = [[0 for i in range(n)] for j in range(n)]
color = [0 for i in range(n)]
tt    = [0]
WHITE = 0
GRAY  = 1
BLACK = 2

def dfs_visit(u):
    color[u] = GRAY
    tt[0] = tt[0] + 1
    d[u] = tt[0]
    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v)
    color[u] == BLACK
    tt[0] = tt[0] + 1
    f[u] = tt[0]

def dfs():
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u)
    for u in range(n):
        print "%d %d %d" %(u + 1, d[u], f[u])

### MAIN
for i in range(n):
    G = map(int, raw_input().split())
    for j in range(G[1]):
        M[G[0]-1][G[2+j]-1] = 1

dfs()
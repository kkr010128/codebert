n = int(raw_input())
N = 100
WHITE = 0
GRAY = 1
BLACK = 2
Color = [WHITE for i in range(n)]
#M = [[0 for i in range(N)] for j in range(N)]
tt = 0
d = [0 for i in range(n)]
f = [0 for i in range(n)]
def dfs_visit(u):
    Color[u] = GRAY
    global tt
    tt += 1
    d[u] = tt
    for v in range(n):
        if M[u][v] == 0:
            continue
        if Color[v] == WHITE:
            dfs_visit(v)
    Color[u] = BLACK 
    tt += 1
    f[u] = tt
 
def dfs():
    #Color = [WHITE for i in range(n)]
    tt = 0
     
    for u in range(n):
        if Color[u] == WHITE:
            dfs_visit(u)
    for u in range(n):
        print "%d %d %d" %(u + 1, d[u], f[u])
 
M = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    tmp = map(int, raw_input().split())
    u = tmp[0]
    k = tmp[1]
    u -= 1
    for j in range(k):
        v = tmp[j + 2]
        v -= 1
        M[u][v] = 1
dfs()
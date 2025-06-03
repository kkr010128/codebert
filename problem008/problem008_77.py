n = int(input())
A = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in range(tmp[1]):
        A[tmp[0]-1][tmp[i+2]-1] = True

WHITE = 0
GRAY = 1
BLACK = 2
color = [WHITE for _ in range(n)]
d = [0 for _ in range(n)]
f = [0 for _ in range(n)]
time = 1

def dfs(u):
    global dfs_color, d, f, time
    color[u] = GRAY
    d[u] += time
    time += 1
    for v in range(n):
        if A[u][v]:
            if color[v] == WHITE:
                dfs(v)
        else:
            continue
    color[u] = BLACK
    f[u] = time
    time += 1 

for u in range(n):
    if color[u] == WHITE:
        dfs(u)

for i in range(n):
    print(str(i+1) + ' ' + str(d[i]) + ' ' + str(f[i]) )
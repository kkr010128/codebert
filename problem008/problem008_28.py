
WHITE = 0
GRAY = 1
BLACK = 2

NIL = -1


def dfs(u):
    global time
    color[i] = GRAY
    time += 1
    d[u] = time
    for v in range(n):
        if m[u][v] and (color[v] == WHITE):
            dfs(v)
        color[u] = BLACK
    time += 1
    f[u] = time


def next(u):
    for v in range(nt[u], n + 1):
        nt[u] = v + 1
        if m[u][v]:
            return v
    return NIL
            


n = int(input())

m = [[0 for i in range(n + 1)] for j in range(n + 1)]
vid = [0] * n
d = [0] * n
f = [0] * n
S = []
color = [WHITE] * n
time = 0
nt = [0] * n

tmp = []
for i in range(n):
    nums=list(map(int,input().split()))
    tmp.append(nums)
    vid[i] = nums[0]

for i in range(n):
    for j in range(tmp[i][1]):
        m[i][vid.index(tmp[i][j + 2])] = 1

for i in range(n):
    if color[i] == WHITE:
        dfs(i)

for i in range(n):
    print(vid[i], d[i], f[i])





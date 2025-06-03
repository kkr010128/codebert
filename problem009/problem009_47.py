
import queue

WHITE = 0
GRAY = 1
BLACK = 2

NIL = -1
INF = 1000000000


def bfs(u):
    global Q
    Q.put(u)
    for i in range(n):
        d[i] = NIL
    d[u] = 0
    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if (m[u][v] == 1) and (d[v] == NIL):
                d[v] = d[u] + 1
                Q.put(v)
n = int(input())

m = [[0 for i in range(n + 1)] for j in range(n + 1)]
vid = [0] * n
d = [0] * n
f = [0] * n
Q = queue.Queue()
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

bfs(0)

for i in range(n):
    print(vid[i], d[i])





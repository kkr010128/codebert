time = 0

def dfs_visit(g, u):
    global time
    time += 1
    u[2] = time
    u[1] = 'g'

    for v in u[0]:
        ch = g[v]
        if ch[1] == 'w':
            ch[4] = u[5]
            dfs_visit(g, ch)
    u[1] = 'b'
    time += 1
    u[3] = time

n = int(input())

g = {}
s = 0
stack = []
for i in range(n):
    x = list(map(int, input().split()))
    g[x[0]] = [x[2:], 'w', 0, 0, None, x[0]]
    if i == 0:
        s = x[0]

for k, v in g.items():
    if v[1] == 'w':
        dfs_visit(g, v)


for i in range(n):
    node = g[i+1]
    print("{} {} {}".format(i+1, node[2], node[3]))
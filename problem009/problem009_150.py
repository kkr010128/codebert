from collections import deque
n = int(input())
G = [[0]*n for _ in range(n)]
for _ in range(n):
    u, k, *V = map(int, input().split())
    if k == 0:
        continue
    else:
        for v in V:
            G[u-1][v-1] = 1



def bfs(u=0):
    Q = deque([])
    color = ['White']*n
    d = [-1]*n

    d[0] = 0
    Q.append(u)
    while Q:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] == 1 and color[v] == 'White':
                if d[v] != -1:
                    continue
                color[v] = 'Gray'
                d[v] = d[u] + 1
                Q.append(v)
        color[u] = 'Black'

    return d

D = bfs()
for i in range(n):
    print('{} {}'.format(i+1, D[i]))


from collections import deque
def bfs(s):
    color[s] = 'GRAY'
    d[s] = 0
    Q.append(0)
    while len(Q) != 0:
        u = Q.popleft()
        for v in range(n):
            if M[u][v] and color[v] == 'WHITE':
                color[v] = 'GRAY'
                d[v] = d[u] + 1
                Q.append(v)
        color[u] = 'BLACK'
        
n = int(input())
M = [[0] * n for _ in range(n)]
color = ['WHITE'] * n
d = [-1] * n
Q = deque()

for _ in range(n):
    a = list(map(int, input().split()))
    u = a[0]
    v = a[2:]
    for j in v:
        M[u - 1][j - 1] = 1
        
bfs(0)

for i in range(n):
    out = ''
    out += '{} {}'.format(i + 1, d[i])
    print(out)
from collections import deque
n = int(input())
M = [[0]*n for _ in range(n)]
d = [-1]*n
st = [0]*n
for _ in range(n):
    i = [int(i) for i in input().split()]
    u = i[0]
    k = i[1]
    V = i[2:]
    for v in V: M[u-1][v-1] = 1

def bfs(s):
    Q = deque()
    Q.append(s)
    st[s] = 1
    d[s] = 0
    while Q:
        u = Q.popleft()
        for v in range(n):
            if M[u][v] and st[v] == 0:
                st[v] = 1
                Q.append(v)
                d[v] = d[u]+1
        st[u] = 2
    return

bfs(0)
for i in range(n): print(i+1,d[i])

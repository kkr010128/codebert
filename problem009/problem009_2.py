n = int(input())
Adj = [[0 for i in range(n)] for i in range(n)]
 
for i in range(n):
    u = list(map(int, input().split()))
    if u[1] > 0:
        for i in u[2: 2 + u[1]]:
            Adj[u[0] - 1][i - 1] = 1
 
color = [0] * n
d = [-1] * n
import queue
Q = queue.Queue()

color[0] = 1
d[0] = 0
Q.put(1)
while not Q.empty():
    u = Q.get()
    for v in range(1, n+1):
        if Adj[u-1][v-1] == 1 and color[v-1] == 0:
            color[v-1] = 1
            d[v-1] = d[u-1] + 1
            Q.put(v)
    color[u-1] = 2

for i in range(n):
    print("{} {}".format(i + 1, d[i]))
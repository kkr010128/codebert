import sys
 
input = sys.stdin.buffer.readline
 
n, m, limit = map(int, input().split())
infi = 10 ** 15
graph = [[infi] * (n + 1) for _ in range(n + 1)]
step = [[infi] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] <= limit:
            graph[i][j] = 1
        elif graph[i][j] == 0:
            graph[i][j] = 0
        else:
            graph[i][j] = infi
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
 
 
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    if graph[a][b] == infi:
        graph[a][b] = 0
    print(graph[a][b] - 1 if graph[a][b] != infi else -1)
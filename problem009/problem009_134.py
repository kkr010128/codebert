
def BFS(s = 0):
    Q.pop(0)
    color[s] = 2
    for j in range(len(color)):
        if A[s][j] == 1 and color[j] == 0:
            Q.append(j)
            color[j] = 1
            d[j] = d[s] + 1
    if len(Q) != 0:
        BFS(Q[0])

n = int(raw_input())
A = [0] * n
for i in range(n):
    A[i] = [0] * n

for i in range(n):
    value = map(int, raw_input().split())
    u = value[0] - 1
    k = value[1]
    nodes = value[2:]
    for j in range(k):
        v = nodes[j] - 1
        A[u][v] = 1

color = [0] * n
Q = [0]
d = [-1] * n
d[0] = 0

BFS(0)

for i in range(n):
    print(str(i + 1) + " " + str(d[i]))
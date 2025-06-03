
def DFS(n = 1, A = [0], i = 0, d = [0], f = [0], time = 1):
    for j in range(n):
        if A[i][j] == 1 and d[j] == 0:
            time = time + 1
            d[j] = time
            time = DFS(n, A, j, d, f, time)
    time = time + 1
    f[i] = time
    return time

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

d = [0] * n
f = [0] * n

time = 0
for i in range(n):
    if d[i] == 0:
        time = time + 1
        d[i] = time
        time = DFS(n, A, i, d, f, time)

for i in range(n):
    print(str(i + 1) + " " + str(d[i]) + " " + str(f[i]))
def DFS(s, t):
    t += 1
    flag[s] = 1
    d[s] = t
    for i in range(1, n+1):
        if G[s][i] == 1:
            if flag[i] == 0:
                DFS(i, t)
                t = f[i]
    f[s] = t + 1

n = int(raw_input())
G = [[0 for i in range(n+1)] for j in range(n+1)]
d = [0 for i in range(n+1)]
f = [0 for i in range(n+1)]

for i in range(n):
    v = map(int, raw_input().split())
    for j in range(v[1]):
        G[v[0]][v[2+j]] = 1

flag = [0 for i in range(n+1)]
for i in range(1, n+1):
    if flag[i] == 0:
        DFS(i, max(f))

for i in range(1, n+1):
    print(str(i) + " " + str(d[i]) + " " + str(f[i]))
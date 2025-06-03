from sys import stdin
n = int(stdin.readline())
M = [0] + [list(map(int, stdin.readline().split()[2:])) for i in range(n)]
sndf = [0] + [[False, i] for i in range(1, n + 1)]
tt = 0
def dfs(u):
    global tt
    sndf[u][0] = True
    tt += 1
    sndf[u].append(tt)
    for v in M[u]:
        if not sndf[v][0]:
            dfs(v)
    tt += 1
    sndf[u].append(tt)
for i in range(1, n + 1):
    if not sndf[i][0]:
        dfs(i)
    print(*sndf[i][1:])
n = int(input())
g = [[] for _ in range(n+1)] #1-index
for i in range(n):
    u, k, *v = map(int, input().split())
    for j in v:
        g[u].append(j)

#-------------------------------------------
def dfs(v): #未訪問の点vから潜っていく
    global time
    seen[v] = 1 #訪問済にする
    time += 1
    d[v] = time
    if g[v]:
        for next_v in g[v]:
            if seen[next_v] == 1: continue
            dfs(next_v) #再帰
    
    time += 1
    f[v] = time
    
#-------------------------------------------
seen = [0]*(n+1) #1-index
seen[0] = 1
seen[1] = 1 
d = [0]*(n+1)
f = [0]*(n+1)
time = 0

dfs(1) #深堀り

for i in range(1,n+1): #孤立点対応
    if seen[i] == 0:
        dfs(i)

for i in range(1,n+1):
    print(i, d[i], f[i])


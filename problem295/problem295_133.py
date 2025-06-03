n,m,l=map(int,input().split())
g=[[999999999999 if i!=j else 0 for j in range(n)] for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a,b=a-1,b-1
    if c>l:
        continue
    g[a][b]=c
    g[b][a]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j]>g[i][k]+g[k][j]:
                g[i][j] = g[i][k]+g[k][j]

for i in range(n):
    for j in range(n):
        if g[i][j]<=l:
            g[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j]>g[i][k]+g[k][j]:
                g[i][j] = g[i][k]+g[k][j]

for i in range(int(input())):
    s,t=map(int,input().split())
    s-=1
    t-=1
    print(g[s][t]-1 if g[s][t]-1<99999999999 else -1)


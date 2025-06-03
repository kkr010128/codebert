n,m,L=map(int,input().split(' '))

inf=10**10

d=[[inf]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split(' '))
    d[a-1][b-1]=c
    d[b-1][a-1]=c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                
dl=[[inf]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] <= L:
            dl[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dl[i][j] > dl[i][k] + dl[k][j]:
                dl[i][j] = dl[i][k] + dl[k][j]

q=int(input())
for _ in range(q):
    s,t = map(int,input().split(' '))
    if dl[s-1][t-1]==inf:
        print(-1)
    else:
        print(dl[s-1][t-1]-1)
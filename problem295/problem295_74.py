n,m,l=map(int,input().split())
cost=[[10**9+1]*n for i in range(n)]
length=[[10**9]*n for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    cost[a][b]=c
    cost[b][a]=c
q=int(input())
st=[map(int,input().split())for i in range(q)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])
for i in range(n):
    length[i][i]=0
for i in range(n):
    for j in range(n):
        if cost[i][j]<=l:
            length[i][j]=0
for k in range(n):
    for i in range(n):
        for j in range(n):
            length[i][j]=min(length[i][j],length[i][k]+length[k][j]+1)
for s,t in st:
    ch=min(length[s-1][t-1],length[t-1][s-1])
    print(-1 if ch>10**8 else ch)
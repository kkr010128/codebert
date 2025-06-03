n,m,l=map(int,input().split())
abc=[list(map(int,input().split())) for _ in [0]*m]
q=int(input())
st=[list(map(int,input().split())) for _ in [0]*q]
inf=10**12
dist=[[inf]*n for _ in [0]*n]
for i in range(n):
    dist[i][i]=0
for a,b,c in abc:
    dist[a-1][b-1]=c
    dist[b-1][a-1]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
inf=10**3
dist2=[[inf]*n for _ in [0]*n]
for i in range(n):
    for j in range(n):
        if dist[i][j]<=l:
            dist2[i][j]=1
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist2[i][j]=min(dist2[i][j],dist2[i][k]+dist2[k][j])
for i in range(n):
    for j in range(n):
        if dist2[i][j]==inf:
            dist2[i][j]=-1
        else:
            dist2[i][j]-=1
for s,t in st:
    print(dist2[s-1][t-1])
n,m,l=map(int,input().split())

a=[list(map(int,input().split())) for i in range(n)]
b=[list(map(int,input().split())) for i in range(m)]
ans=[[0]* l for i in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            ans[i][j]+=b[k][j]*a[i][k]
    print(*ans[i])

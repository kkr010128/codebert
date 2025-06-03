cost,m,=map(int,input().split())
c=list(map(int,input().split()))
DP=[[10**10 for i in range(60001)] for j in range(21)]
for i in range(m):
    DP[i][c[i]]=1
    for j in range(60001):
        if c[i]>j:
            if i==0:
                DP[i][j]=0
            else:DP[i][j]=DP[i-1][j]
        elif j+c[i]<=60000:
            DP[i][j]=min(DP[i][j-c[i]]+1,DP[i-1][j])
print(DP[m-1][cost])

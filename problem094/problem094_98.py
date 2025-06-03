R,C,K=map(int,input().split())

Value=[[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r,c,v=map(int,input().split())
    Value[r][c]=v

DP=[[0,0,0,0] for _ in range(C+1) ]

for y in range(1,R+1):
    #下に移動
    for x in range(1,C+1):
        DP[x][0]=max(DP[x])
        DP[x][1]=DP[x][0]+Value[y][x]
        DP[x][2]=DP[x][3]=0

    #右に移動
    for x in range(1,C+1):
        for k in range(0,3+1):
            DP[x][k]=max(DP[x][k],DP[x-1][k])

        for k in range(1,3+1):
            DP[x][k]=max(DP[x][k],DP[x-1][k-1]+Value[y][x])

print(max(DP[-1]))
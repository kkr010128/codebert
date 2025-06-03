N = int(input())
_L = list(map(int,input().split()))
L = [(v,i) for i,v in enumerate(_L)]
L = sorted(L,key=lambda x:(-x[0]))

dp = [[0]*(N+1) for _ in range(N+1)]

ans=0
for x in range(N):#前から
    for y in range(N):#後ろから
        cur = x+y
        if  cur==N:
            ans = max(ans,dp[x][y])
            break
        val,ind = L[cur]
        dp[x+1][y] = max(dp[x+1][y],dp[x][y]+val*abs(ind-x))
        dp[x][y+1] = max(dp[x][y+1],dp[x][y]+val*abs(N-y-1-ind))
print(ans)

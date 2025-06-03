H,N = map(int,input().split())
Magic = [list(map(int, input().split())) for i in range(N)]

inf = float("inf")
dp = [inf]*(H+1)
dp[0]=0

for i in range(N):
    a,b = Magic[i]
    for h in range(H):
        
        next_h = min(h+a,H)
        dp[next_h]=min(dp[next_h],dp[h]+b)

print(dp[-1])
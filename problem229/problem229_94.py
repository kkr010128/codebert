H,N = map(int,input().split())
Q = []
for _ in range(N):
    a,b = map(int,input().split())
    Q.append((a,b))
INF = float("inf")
dp = [INF]*(H+1)
dp[0] = 0
for i in range(H+1):
    for a,b in Q:
        if i+a>=H:
            dp[H] = min(dp[H],dp[i]+b)
        else:
            dp[i+a] = min(dp[i+a],dp[i]+b)
print(dp[-1])
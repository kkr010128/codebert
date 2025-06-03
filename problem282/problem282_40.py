N,T=map(int,input().split())
G=[list(map(int,input().split())) for _ in range(N)]

G.sort()
dp=[0]*(60000)
for g in G:
    for i in range(T-1,-1,-1):
        dp[i+g[0]]=max(dp[i+g[0]],dp[i]+g[1])
print(max(dp))

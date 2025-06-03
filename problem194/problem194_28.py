H, W=map(int, input().split())
S=[]
from math import ceil

for h in range(H):
    s=list(input())
    S.append(s)

dp = [[float("INF")]*W for _ in range(H)]
if S[0][0]=="#":
    dp[0][0]=1
else:
    dp[0][0]=0

for h in range(H):
    for w in range(W):
        if w==0 and h==0:
            continue
        if h==0:
            if S[h][w] == S[h][w-1]:
                now=0
            else:
                now=1
            dp[h][w]=min(dp[h][w-1]+now, dp[h][w])
        elif w==0:
            if S[h][w] == S[h-1][w]:
                now=0
            else:
                now=1
            dp[h][w]=min(dp[h-1][w]+now, dp[h][w])
        else:
            if S[h][w]==S[h][w-1]:
                noww = 0
            else:
                noww=1
            if S[h][w]==S[h-1][w]:
                nowh = 0
            else:
                nowh=1
            dp[h][w] = min(dp[h][w], dp[h][w-1]+noww, dp[h-1][w]+nowh)
ans = ceil(dp[-1][-1]/2)
print(ans)
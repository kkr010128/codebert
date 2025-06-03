"""
時間がかかる料理は、食べるとしたら最後に食べるのがベスト。
逆にいうと、その料理を食べるかどうかを検討する段階ではほかの料理は食べるかどうかの検討は終わっている状態。
なので、食べるのにかかる時間でソートしてナップサックすればよい。
"""

N,T = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(T)
AB.sort()

ans = 0
for i in range(N):
    a,b = AB[i]
    ans = max(ans,dp[-1]+b)
    for j in range(T-1,-1,-1):
        if j-a >= 0:
            dp[j] = max(dp[j],dp[j-a]+b)
print(ans)
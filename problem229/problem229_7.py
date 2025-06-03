h,n=map(int,input().split())
magic=[list(map(int,input().split())) for _ in range(n)]
dp=[10**9]*(h+10**5)
#dp[i]:敵の体力をi減らすのに必要な魔力の最小値
dp[0]=0
for i in range(h):
    for damage,cost in magic:
        dp[i+damage]=min(dp[i+damage],dp[i]+cost)
ans=10**9
for i in range(10**5):
    ans=min(ans,dp[i+h])
print(ans)
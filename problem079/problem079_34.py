s=int(input())
if s==1:
    print(0)
    exit()
mod=10**9+7
dp=[0]*(s+1)
dp[1]=0
dp[2]=0

for i in range(3,s+1):
    for j in range(3,i+1):
        dp[i]+=(dp[i-j])%mod
    dp[i]+=1

print(dp[s]%mod)
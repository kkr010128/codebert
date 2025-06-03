n,k = map(int,input().split())
sec = []
for i in range(k):
  l,r = map(int,input().split())
  sec.append([l,r])

mod = 998244353
dp = [0]*(n+1)
dp[0],dp[1] = 0,1
cumsum = [0]*(n+1)
cumsum[1] = 1
for i in range(2,n+1):
  for l,r in sec:
    if i>l:
      dp[i] += cumsum[i-l]-cumsum[max(0,i-r-1)]
  cumsum[i] = (dp[i]+cumsum[i-1])%mod
print(dp[n]%mod)
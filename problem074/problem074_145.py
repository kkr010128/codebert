N,K = [int(i) for i in input().split()]
mod = 998244353
LR = []
S = []
dp = [0]*(N+1)
dps = [0]*(N+1)
dps[1] = 1
dp[1] = 1
for i in range(K):
  LR.append([int(i) for i in input().split()])

for i in range(1,N+1):
  for l,r in LR:
    l,r = i - r,i - l
    #print(l,r)
    if r < 1:
      continue
    l = max(1,l)
    dp[i] += dps[r] - dps[l-1]
    dp[i] %= mod
    #print(dp[i])
    
  dps[i] = dps[i-1] + dp[i]
  #print(dp, dps)
print(dp[-1])
n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
  dpi = 10 ** 9
  for j in range(m):
    if(i-c[j]>=0):
      tmp = dp[i-c[j]] + 1
      if(tmp < dpi):
        dpi = tmp
  dp[i] = dpi
  
  
print(dp[n])

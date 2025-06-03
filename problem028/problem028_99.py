n, m = map(int, input().split())
c = list(map(int, input().split()))
c.sort() # sortしなくてもこのアルゴリズムは有効

dp = [50001 for i in range(n + 1)]
dp[0] = 0

for i in c:
  for j in range(i, n + 1):
    dp[j] = min(dp[j], dp[j - i] + 1)
    
print(dp[n])

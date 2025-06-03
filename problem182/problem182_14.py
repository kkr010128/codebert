n, k, c = map(int, input().split())
s = input()

def solve_dp(s):
  dp = [0]*(n+2)
  for i in range(n):
    if i <= c and s[i] == 'o':
      dp[i+1] = 1
    else:
      if s[i] == 'o':
        dp[i+1] = max(dp[i], dp[i-c]+1)
      else:
        dp[i+1] = dp[i]
  return dp

mae = solve_dp(s)
ushiro = solve_dp(s[::-1])[::-1]

for i in range(1,n+1):
  if mae[i-1] + ushiro[i+1] < k:
    print(i)
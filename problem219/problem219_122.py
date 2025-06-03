s = input(); n = len(s)
dp = [ [0,1<<32] for i in range(2) ]
for i in range(n):
  d = ord(s[i])-ord('0')
  dp[(i+1)%2][0] = min(dp[i%2][0], dp[i%2][1])+d
  dp[(i+1)%2][1] = min(dp[i%2][0], dp[i%2][1]-2)+11-d
print(min(dp[n%2][0],dp[n%2][1]))
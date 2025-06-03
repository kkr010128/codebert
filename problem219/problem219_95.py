s = input()
s = "".join([ i for i in reversed(s)]) + "0"
 
INF = 10 ** 32
n = len(s)
dp = [ [INF]*2 for _ in range(n)]
 
dp[0][0] = 0
 
for i in range(n-1):
    x = int(s[i])
    dp[i+1][0] = min( dp[i][0]+x, dp[i][1]+x )
    dp[i+1][1] = min( dp[i][0]+1+(10-x), dp[i][1]+(9-x) )
 
print(min(dp[n-1][0], dp[n-1][1]))
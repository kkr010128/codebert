n = int(input())
a = list(map(int,input().split()))
num  = []
for i in range(n):
    num.append([a[i],i])
num.sort(reverse = True)
dp = [[0]*(n+1)for i in range(n+1)]
ans = 0
for l in range(n):
    for r in range(n):
        if l+r == n:
            ans = max(ans,dp[l][r])
            break
        dp[l+1][r] = max(dp[l+1][r], dp[l][r] + num[l+r][0]*abs(num[l+r][1]-l))
        dp[l][r+1] = max(dp[l][r+1],dp[l][r]+num[l+r][0]*abs(num[l+r][1]-n+1+r))
print(ans)
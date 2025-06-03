from sys import stdin
n = int(stdin.readline())
ans = 0
dp = [0]*(n+1)
for i in range(1,n+1):
    j = i
    while j <= n:
        dp[j] += 1
        j += i
for i in range(1,n+1):
    ans += dp[i]*i
print(ans)
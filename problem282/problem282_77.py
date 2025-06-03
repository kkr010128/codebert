import sys
readline = sys.stdin.buffer.readline

n,t = map(int,readline().split())

dp = [0]*(t+1)

AB = [list(map(int,readline().split())) for i in range(n)]
AB.sort(reverse=True)
for i in range(n):
    a,b = AB[i]
    for j in range(t):
        if j+a > t:
            dp[j] = max(dp[j],b)
        else:
            dp[j] = max(dp[j],dp[j+a]+b)

print(dp[0])
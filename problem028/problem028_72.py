import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*c = map(int,read().split())
INF = 9**9
dp = [INF] * (n+1)

dp[0] = 0
for i in range(1,n+1):
    for j in c:
        if i-j>= 0:
            dp[i] = min(dp[i],dp[i-j]+1)

print(dp[n])


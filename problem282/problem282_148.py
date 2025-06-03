import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,t = list(map(int, input().split()))
ab = [None]*n
for i in range(n):
    ab[i] = tuple(map(int, input().split()))
ab.sort()
dp = [[0]*(t) for _ in range(n)]
for i in range(1, n):
    a,b = ab[i-1]
    for j in range(t-1, 0, -1):
        dp[i][j] = dp[i-1][j]
        if j>=a and dp[i][j]<dp[i-1][j-a]+b:
            dp[i][j] = dp[i-1][j-a]+b
ans = max((dp[i][t-1] + ab[i][1]) for i in range(n))
print(ans)
import sys
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = ni()
a = na()
b = []
for i in range(n):
    b.append((a[i],i))
 
b.sort(reverse=True)

dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    x,y = b[i-1]
    for j in range(i+1):
        left = dp[i-1][j-1] + x*abs(y-j+1) if j > 0 else -1
        right = dp[i-1][j] + x*abs(n-i+j-y) if j < i else -1
        dp[i][j] = max(left,right)

print(max(dp[-1]))
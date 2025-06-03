import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

n, s = nm()
a = nl()
mod = 998244353
dp = [0]*(s+1)
dp[0] = 1
for i in range(n):
    v = a[i]
    for j in range(s, -1, -1):
        if j >= v:
            dp[j] = (dp[j] * 2 + dp[j-v]) % mod
        else:
            dp[j] = dp[j] * 2 % mod
print(dp[s])
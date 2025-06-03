import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

n = int(readline())
# O(N)解法
ans = 0
for i in range(1,n+1):
    a = n//i
    ans += a*(a+1)*i//2
print(ans)

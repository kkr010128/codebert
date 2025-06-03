import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N = int(readline())
a = list(map(int,readline().split()))

s = 0
for ai in a:
    s = s^ai
ans = []
for ai in a:
    ans.append(s^ai)
print(' '.join(map(str,ans)))

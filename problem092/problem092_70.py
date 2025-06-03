import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

x,k,d = map(int,readline().split())

x = abs(x)
if (x >= k*d):
    print(x-k*d)
elif ((k-x//d)%2):
    print(abs(x%d-d))
else:
    print(x%d)

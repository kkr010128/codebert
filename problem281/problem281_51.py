import sys
from functools import reduce
X, Y = map(int, input().split())
mod = 10**9 + 7

if (X+Y)%3 != 0:
    print(0)
    sys.exit()

if 2 * min(X, Y) < max(X, Y):
    print(0)
    sys.exit()

def f(n, A):
    if A == 0:
        return 1
    bunsi = reduce(lambda x, y: x*y%mod, range(n, n-A, -1))
    bunbo = reduce(lambda x, y: x*y%mod, range(1, A+1))
    return bunsi * pow(bunbo, mod-2, mod) % mod

ans = 0
r, d = 0, 0
if X == Y:
    r, d = X//3, Y//3
    ans = f(r+d, d)%mod
else:
    r = abs(X-Y) + ((X+Y) - 3*abs(X-Y))//6
    d = ((X+Y) - 3*abs(X-Y))//6
    ans = f(r+d, d)%mod

print(ans)
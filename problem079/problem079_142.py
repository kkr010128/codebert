MOD = 10 ** 9 + 7

from operator import mul
from functools import reduce

def nCr(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under



S = int(input())
ans = 0
for i in range(1, S):
    if S - i * 3 < 0:
        break
    ans += nCr(S - i * 3 + i - 1, i - 1)
print(ans % MOD)
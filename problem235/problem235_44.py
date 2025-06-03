from fractions import gcd
from functools import reduce, lru_cache

MOD = 10**9+7
N = int(input())
A = list(map(int, input().split()))

def lcm(x, y):
    return int(x*y)//int(gcd(x, y))

B = [1 for i in range(N)]
global_lcm = reduce(lcm, A) % MOD
ans = 0
for i in range(N):
    ans += (global_lcm*pow(A[i], MOD-2, MOD)) % MOD
    ans %= MOD

print(ans)
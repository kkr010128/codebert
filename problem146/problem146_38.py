from collections import defaultdict
from math import gcd


MOD = 1000000007
N = int(input())
both_zeros_cnt = 0
bads = defaultdict(lambda: [0, 0])
for _ in range(N):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        both_zeros_cnt += 1
        continue
    if B < 0 or (B == 0 and A < 0):
        A, B = -A, -B
    g = gcd(A, B)
    A, B = A // g, B // g
    if A > 0:
        bads[(A, B)][0] += 1
    else:
        bads[(B, -A)][1] += 1


NMAX = 2 * 10 ** 5 + 1
pow2 = [1] * (NMAX + 1)
for i in range(1, NMAX + 1):
    pow2[i] = pow2[i - 1] * 2 % MOD
ans = 1
for k, l in bads.values():
    ans *= pow2[k] + pow2[l] - 1
    ans %= MOD
print((ans + both_zeros_cnt - 1) % MOD)

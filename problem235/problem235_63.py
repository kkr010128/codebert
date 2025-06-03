# https://atcoder.jp/contests/abc152/tasks/abc152_e

# 1 <= i < j <= N (i < j)について AiBi = AjBjが成り立つBの和の最小値
# LCM/Ai

from collections import defaultdict
from math import gcd

MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

lcm = A[0]
for a in A:
    lcm = (lcm * a) // gcd(lcm, a)
lcm %= MOD

# フェルマーの小定理 a^{P-1} = 1 (mod P)
ans = 0
for a in A:
    ans += lcm * pow(a, MOD - 2, MOD) % MOD
    ans %= MOD
print(ans)
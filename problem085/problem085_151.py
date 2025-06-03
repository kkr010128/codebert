from math import gcd
from functools import reduce

n = int(input())
A = list(map(int, input().split()))
res = ['pairwise coprime', 'setwise coprime', 'not coprime']

MAX = 10 ** 6 + 1000
dp = [i for i in range(MAX)]
# dp[x]はxを割り切る最小の素数
for x in range(2, MAX):
    if dp[x] < x: continue
    for y in range(x + x, MAX, x):
        if dp[y] == y:
            dp[y] = x

def get_factor(n):
    factors = []
    while n > 1:
        factors.append(dp[n])
        n //= dp[n]
    return factors

prime_factors = []
for a in A:
    factor = get_factor(a)
    factor_set = list(set(factor))
    prime_factors.extend(factor_set)

if len(prime_factors) == len(set(prime_factors)):
    print(res[0])
elif reduce(gcd, A) == 1:
    print(res[1])
else:
    print(res[2])

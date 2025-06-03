from sys import stdin
from collections import deque, Counter, defaultdict
# from fractions import gcd
from math import gcd
import heapq

MOD = 10 ** 9 + 7
input = stdin.readline

n = int(input())
zero = 0
A, B = [], []
# mp = defaultdict(lambda: [0, 0])
mp = {}
for i in range(n):
    ai, bi = map(int, input().split())
    if ai == 0 and bi == 0:
        zero += 1
        continue

    gi = gcd(ai, bi)
    ai = ai // gi
    bi = bi // gi

    if bi < 0:
        ai = -ai
        bi = -bi
    if bi == 0 and ai < 0:
        ai = -ai
    if ai <= 0:
        ai, bi = bi, -ai
        if (ai, bi) in mp:
            mp[(ai, bi)][0] += 1
        else:
            mp[(ai, bi)] = [1, 0]
    else:
        if (ai, bi) in mp:
            mp[(ai, bi)][1] += 1
        else:
            mp[(ai, bi)] = [0, 1]

ans = 1
for key in mp:
    s, t = mp[key]
    ans *= pow(2, s, MOD) + pow(2, t, MOD) - 1
    ans %= MOD
print((zero - 1 + ans) % MOD)